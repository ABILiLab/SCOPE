import os
import pickle
import pandas as pd
from torch.autograd import Variable
from sklearn import metrics
from scope_model_utils import *
import time
from tabulate import tabulate


# Please modify only this log directory for your local environment.
LOG_PATH = './logs/deepgcn_with_gaussion_weight'
SAVE_PATH = os.path.join(LOG_PATH, str(int(time.time())))
os.makedirs(SAVE_PATH, exist_ok=True)

class TestDataset(Dataset):
    def __init__(self, dataframe,data_path):
        self.names = dataframe['ID'].values
        self.sequences = dataframe['sequence'].values
        self.labels = dataframe['label'].values
        self.data_path = data_path

    def __getitem__(self, index):
        sequence_name = self.names[index]
        sequence = self.sequences[index]
        label = np.array(self.labels[index])
        data_path = self.data_path

        pssm_feature,hmm_feature,evo_feature = embedding(sequence_name,data_path)
        atom_features,seq_feature = get_atom_features(sequence_name, data_path)
        node_features = np.concatenate([pssm_feature, hmm_feature, atom_features, seq_feature], axis=1)
        graph = load_graph(sequence_name,data_path)
        return sequence_name, sequence, label[:1000], node_features[:1000], graph[:1000,:1000], evo_feature[:1000], atom_features[:1000]

    def __len__(self):
        return len(self.labels)


def train_one_epoch(model, data_loader, epoch, data_path):
    epoch_loss_train = 0.0
    n = 0
    update_ecfeas = {}
    for i, data in enumerate(data_loader):
        model.optimizer.zero_grad()
        sequence_name, _, labels, _, node_features, graphs, evo_feature = data
        if torch.cuda.is_available():
            node_features = Variable(node_features.cuda())
            graphs = Variable(graphs.cuda())
            evo_feature = Variable(evo_feature.cuda())
            y_true = Variable(labels.cuda())
        else:
            node_features = Variable(node_features)
            graphs = Variable(graphs)
            evo_feature = Variable(evo_feature)
            y_true = Variable(labels)

        node_features = torch.squeeze(node_features)
        graphs = torch.squeeze(graphs)
        evo_feature = torch.squeeze(evo_feature)
        y_true = torch.squeeze(y_true)

        y_pred, ec_fea, gs_pred = model(node_features, graphs, evo_feature)

        ec_fea = torch.unsqueeze(ec_fea, 0)
        update_ecfeas[sequence_name[0]] = ec_fea

        funsite_loss = model.criterion(y_pred, y_true)
        gs_loss = model.criterion(gs_pred, y_true)
        gs_weight = 0.0001
        loss =funsite_loss + gs_weight * gs_loss

        model.optimizer.zero_grad()
        loss.backward()
        model.optimizer.step()
        epoch_loss_train += funsite_loss.item()
        n += 1

    epoch_loss_train_avg = epoch_loss_train / n

    if (epoch+1) % 10 == 0:
        print("this epoch is ", epoch)
        f_save = open(data_path + 'updated_enzfeas/dict_enzfeas.pkl', 'wb')
        pickle.dump(update_ecfeas, f_save)
        f_save.close()
    return epoch_loss_train_avg


def evaluate(model, data_loader):
    model.eval()

    epoch_loss = 0.0
    n = 0
    valid_pred = []
    valid_true = []
    pred_dict = {}

    for data in data_loader:
        with torch.no_grad():
            sequence_names, sequence, labels, node_features, graphs, evo_feature, atom_features = data

            if torch.cuda.is_available():
                node_features = Variable(node_features.cuda())
                graphs = Variable(graphs.cuda())
                evo_feature = Variable(evo_feature.cuda())
                y_true = Variable(labels.cuda())
            else:
                node_features = Variable(node_features)
                graphs = Variable(graphs)
                evo_feature = Variable(evo_feature)
                y_true = Variable(labels)

            node_features = torch.squeeze(node_features)
            graphs = torch.squeeze(graphs)
            evo_feature = torch.squeeze(evo_feature)
            y_true = torch.squeeze(y_true)
            y_pred,_,_ = model(node_features, graphs, evo_feature)#
            loss = model.criterion(y_pred, y_true)

            softmax = torch.nn.Softmax(dim=1)
            y_pred = softmax(y_pred/8)
            y_pred = y_pred.cpu().detach().numpy()
            y_true = y_true.cpu().detach().numpy()
            valid_pred += [pred[1] for pred in y_pred]
            valid_true += list(y_true)
            pred_dict[sequence_names[0]] = [pred[1] for pred in y_pred]

            epoch_loss += loss.item()
            n += 1
    epoch_loss_avg = epoch_loss / n
    return epoch_loss_avg, valid_true, valid_pred, pred_dict


def analysis(y_true, y_pred,best_threshold=None):
    if best_threshold == None:
        best_f1 = 0
        best_threshold = 0
        for threshold in range(0, 100):
            threshold = threshold / 100
            binary_pred = [1 if pred >= threshold else 0 for pred in y_pred]
            binary_true = y_true
            f1 = metrics.f1_score(binary_true, binary_pred)
            if f1 > best_f1:
                best_f1 = f1
                best_threshold = threshold

    binary_pred = [1 if pred >= best_threshold else 0 for pred in y_pred]
    binary_true = y_true

    # binary evaluate
    binary_acc = metrics.accuracy_score(binary_true, binary_pred)
    precision = metrics.precision_score(binary_true, binary_pred)
    recall = metrics.recall_score(binary_true, binary_pred)
    f1 = metrics.f1_score(binary_true, binary_pred)
    AUC = metrics.roc_auc_score(binary_true, y_pred)
    precisions, recalls, thresholds = metrics.precision_recall_curve(binary_true, y_pred)
    AUPRC = metrics.auc(recalls, precisions)
    mcc = metrics.matthews_corrcoef(binary_true, binary_pred)

    results = {
        'binary_acc': binary_acc,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'AUC': AUC,
        'AUPRC': AUPRC,
        'mcc': mcc,
        'threshold': best_threshold
    }
    return results


def train_model(train_dataframe, valid_dataframe, data_path):

    print("Train on", str(train_dataframe.shape[0]), "samples, validate on", str(valid_dataframe.shape[0]), "samples")
    train_loader = DataLoader(dataset=ProDataset(train_dataframe, data_path), batch_size=BATCH_SIZE, shuffle=True, num_workers=2)

    model = SCOPE(NLAYER, INPUT_DIM, HIDDEN_DIM, NUM_CLASSES, DROPOUT)
    if torch.cuda.is_available():
        model.cuda()

    for epoch in range(NUMBER_EPOCHS):
        print("\n========== Train epoch " + str(epoch + 1) + " ==========")
        model.train()
        epoch_time = time.time()


        epoch_loss_train_avg = train_one_epoch(model, train_loader, epoch, data_path)
        print("Epoch: {} cost time: {}, train_loss: {}".format(epoch + 1, time.time() - epoch_time, epoch_loss_train_avg))
        model_save_path = os.path.join(SAVE_PATH,"Model") 
        os.makedirs(model_save_path, exist_ok=True)
        torch.save(model.state_dict(), os.path.join( model_save_path, f'model_weight{epoch:03d}.pth' ))

        # if epoch>4:
        if True:
            valid_record = {}
            table_data = []
            for i in [0,1,2,3,4]:
                result_test  , dataset_name = test_model(model ,i)
                result_test['epoch'] = epoch + 1
                valid_record[dataset_name] = result_test
            for k in valid_record.keys():
                print_data = []
                print_data.append(valid_record[k]['epoch'])
                print_data.append(k)
                print_data.append(valid_record[k]['binary_acc'])
                print_data.append(valid_record[k]['precision'])
                print_data.append(valid_record[k]['recall'])
                print_data.append(valid_record[k]['f1'])
                print_data.append(valid_record[k]['AUC'])
                print_data.append(valid_record[k]['AUPRC'])
                print_data.append(valid_record[k]['mcc'])
                table_data.append(print_data)
            visualize_table = tabulate(table_data, headers=["Epoch","TestSet","Binary Acc","Precision","Recall","F1","AUC","AUPRC","MCC","Train Loss","Vali Loss"])
            print(visualize_table)
            result_save_path = os.path.join(SAVE_PATH,f'test_result_{epoch:03d}.txt')
            with open(result_save_path, 'w') as f:
                f.write(visualize_table)


def main():

    #loading the PDBid for training
    IDs, sequences, labels, EC1 = [], [], [], []
    data_path = "./Dataset/training_data/"
    f = open(data_path + "training_id_withEC.txt", "r")
    filter_list = ['1gkm-A']
    filedata = f.readlines()
    for line in filedata:
        protein = line.strip()
        pdb_id = protein[:4].lower() + "-" + protein[5].upper()
        if(pdb_id in filter_list):
            continue
        IDs.append(pdb_id)
    f.close()
    prot_num = len(IDs)

    #loading the training label
    prot_seq = {}
    prot_anno = {}
    f = open(data_path + "training_label.txt", "r")
    data = f.readlines()
    for line in range(0, len(data)):
        if data[line].startswith('>'):
            protein = data[line].lstrip('>').strip()
            Pro, Chain = protein.split('-') if '-' in protein else protein.split('_')
            pdb_id = Pro.lower() + "-" + Chain.upper()
            seq_p = data[line + 1].strip()
            anno_p = data[line + 2].strip()
            if(pdb_id in filter_list):
                continue
            prot_seq[pdb_id] = seq_p
            prot_anno[pdb_id] = anno_p

    for prot in IDs:
        label_list = []
        if(prot in filter_list):
            continue
        seq = prot_seq[prot]
        label = prot_anno[prot]
        sequences.append(seq)
        for i in range(len(label)):
            label_list.append(int(label[i]))
        labels.append(label_list)
    data_dic = {"ID":IDs, "sequence":sequences, "label":labels }
    data_dataframe = pd.DataFrame(data_dic)

    train_dataframe = data_dataframe.iloc[:int(prot_num * 0.9)]
    valid_dataframe = data_dataframe.iloc[int(prot_num * 0.9):]
    train_model(train_dataframe, valid_dataframe, data_path)


def test_model( model , index = 0):
    dataset = ["NN","HA_superfamily", "EF_superfamily", "PC", "EF_fold"]
    dataset_error_filter =  {
        "NN": ['2adm-A'],
        "HA_superfamily":['1exn-B','1d8h-C','1b6b-A'],
        "EF_superfamily":[],
        "PC":[],
        "EF_fold":[]
    }

    # loading the PDBid for testing
    data_dir = "./Dataset/" + dataset[index] + "/"
    f = open(data_dir + "test-" + dataset[index] + "_id.txt", "r")
    protein_list ,sequences, labels = [], [], []
    filedata = f.readlines()
    for line in filedata:
        protein = line.strip()
        if protein not in dataset_error_filter[dataset[index]]:
            protein_list.append(protein)
    f.close()

    # loading the testing label
    prot_seq = {}
    prot_anno = {}
    f = open(data_dir + dataset[index] +"_enzyme_label.txt", "r")
    data = f.readlines()
    for line in range(0, len(data)):
        if data[line].startswith('>'):
            protein = data[line].lstrip('>').strip()
            PDBID, Chain = protein.split('-') if '-' in protein else protein.split('_')
            pro = PDBID.lower() + "-" + Chain.upper()
            if pro in dataset_error_filter[dataset[index]]:
                continue
            seq_p = data[line + 1].strip()
            query_anno = data[line + 2].strip()
            prot_seq[pro] = seq_p
            prot_anno[pro] = query_anno

    for prot in protein_list:
        label_list = []
        seq = prot_seq[prot]
        label = prot_anno[prot]
        sequences.append(seq)
        for i in range(len(label)):
            label_list.append(int(label[i]))
        labels.append(label_list)

    test_dic = {"ID": protein_list, "sequence": sequences, "label": labels}
    test_dataframe = pd.DataFrame(test_dic)
    data_path = data_dir 

    test_loader = DataLoader(dataset=TestDataset(test_dataframe,data_path), batch_size=BATCH_SIZE, shuffle=True, num_workers=2)

    _, test_true, test_pred, _ = evaluate(model, test_loader)
    result_test = analysis(test_true, test_pred)
    return result_test , dataset[index]


if __name__ == "__main__":
    main()









