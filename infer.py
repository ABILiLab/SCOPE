import os
import pandas as pd
from torch.autograd import Variable
from scope_model_utils import *

class TestDataset(Dataset):
    def __init__(self, dataframe,data_path):
        self.names = dataframe['ID'].values
        self.data_path = data_path

    def __getitem__(self, index):
        sequence_name = self.names[index]
        data_path = self.data_path
        fasta_path = os.path.join(data_path, 'fasta',sequence_name + '.fa')
        with open(fasta_path) as f:
            sequence = f.read().split('\n')[1]


        pssm_feature,hmm_feature,evo_feature = embedding(sequence_name,data_path)
        atom_features,seq_feature = get_atom_features(sequence_name, data_path)
        node_features = np.concatenate([pssm_feature, hmm_feature, atom_features, seq_feature], axis=1)
        graph = load_graph(sequence_name,data_path)
        return sequence_name,sequence , node_features[:1000], graph[:1000,:1000], evo_feature[:1000], atom_features[:1000]

    def __len__(self):
        return len(self.names)

def evaluate(model, data_loader):
    model.eval()
    for data in data_loader:
        with torch.no_grad():
            # sequence_names, _, labels,_, node_features, graphs, evo_feature = data
            sequence_names,seq, node_features, graphs, evo_feature, atom_features = data
            if torch.cuda.is_available():
                node_features = Variable(node_features.cuda())
                graphs = Variable(graphs.cuda())
                evo_feature = Variable(evo_feature.cuda())
            else:
                node_features = Variable(node_features)
                graphs = Variable(graphs)
                evo_feature = Variable(evo_feature)

            node_features = torch.squeeze(node_features)
            graphs = torch.squeeze(graphs)
            evo_feature = torch.squeeze(evo_feature)
            y_pred,_,_ = model(node_features, graphs, evo_feature)#

            softmax = torch.nn.Softmax(dim=1)
            y_pred = softmax(y_pred/8)
            y_pred = y_pred.cpu().detach().numpy()
            save_path = 'InferResult'
            os.makedirs(save_path,exist_ok=True)
            with open(os.path.join(save_path,sequence_names[0]), 'w') as f:
                for i in range(y_pred.shape[0]):
                    f.write(seq[0][i] + '\t' + str(y_pred[i][1]) + '\n')


def main():
    with torch.no_grad():
        model = SCOPE(NLAYER, INPUT_DIM, HIDDEN_DIM, NUM_CLASSES, DROPOUT)
        model.load_state_dict(torch.load('./checkpoints/best.pth',map_location='cpu'))
        if torch.cuda.is_available():
            model.cuda()
        test_model(model)


def test_model( model ):

    # loading the PDBid for testing
    data_dir = "./Example/"
    f = open(data_dir + "pdb_ids.txt", "r")
    protein_list ,sequences  = [], []
    filedata = f.readlines()
    for line in filedata:
        protein = line.strip()
        protein_list.append(protein)
    f.close()
    test_dic = {"ID": protein_list }
    test_dataframe = pd.DataFrame(test_dic)
    data_path = data_dir 
    test_loader = DataLoader(dataset=TestDataset(test_dataframe,data_path), batch_size=BATCH_SIZE, shuffle=True, num_workers=2)
    evaluate(model, test_loader)


if __name__ == "__main__":
    main()