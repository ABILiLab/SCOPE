import math
import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from torch.nn.parameter import Parameter
import h5py

MAP_CUTOFF = 6
INPUT_DIM = 64
HIDDEN_DIM = 512
NLAYER = 3
DROPOUT = 0.1
LEARNING_RATE = 5E-5
BATCH_SIZE = 1
NUM_CLASSES = 2
NUMBER_EPOCHS = 500
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def remove_nan(matrix,padding_value=0.):
    aa_has_nan = np.isnan(matrix).reshape([len(matrix),-1]).max(-1)
    matrix[aa_has_nan] = padding_value
    return matrix

def embedding(sequence_name, data_path):
    pssm_feature = np.load(data_path + "pssm/processed_pssm/" + sequence_name + '.npy')
    hmm_feature = np.load(data_path + "hhm/processed_hhm/" + sequence_name + '.npy')
    with h5py.File(data_path + 'Prot5/train_per_residue_embeddings.h5', "r") as f:
        evo_feature = f[sequence_name][:]
    return pssm_feature, hmm_feature, evo_feature.astype(np.float32)


def get_atom_features(sequence_name, data_path):
    atom_feature = np.load(data_path + 'Atom_feas/matched_atomfea/'+ sequence_name + '.npy')
    atom_feature = remove_nan(atom_feature, padding_value=0.)

    seq_feature = np.load(data_path + 'seqfea/' + sequence_name + '.npy')
    return atom_feature, seq_feature

def normalize(mx):
    rowsum = np.array(mx.sum(1))
    r_inv = (rowsum ** 0.5).flatten()
    for i in range(len(r_inv)):
        r_inv[i] = 0 if r_inv[i] == 0 else 1 / r_inv[i]
    r_mat_inv = np.diag(r_inv)
    result = r_mat_inv @ mx @ r_mat_inv
    return result

def load_graph(sequence_name, data_path):
    #using PDB structure
    dismap = np.load(data_path + "contact_map/" + sequence_name + ".npy")
    mask = ((dismap >= 0) * (dismap <= MAP_CUTOFF))
    adjacency_matrix = mask.astype(np.int16)
    norm_matrix = normalize(adjacency_matrix.astype(np.float32))
    return norm_matrix

class Gaussis(nn.Module):
    def __init__(self, hidden_dim):
        super(Gaussis, self).__init__()
        self.fc1 = nn.Linear(hidden_dim, hidden_dim)
        kernel = self.gaussian_kernel1d(kernel_size=9, sigma=2)
        kernel = kernel.view( 1, 1, -1).repeat( hidden_dim, 1, 1)
        self.register_buffer("weight", kernel)
        self.groups = hidden_dim
        self.kernel_size = 9

    def gaussian_kernel1d(self,kernel_size=9, sigma=2):
        x =  torch.arange(kernel_size).float() -kernel_size//2
        kernel = torch.exp(-(x**2)/(2*sigma**2))
        kernel = kernel / kernel.sum()
        return kernel

    def forward(self, x):
        x_t = x.transpose(0, 1)
        out = F.conv1d(
            x_t, weight=self.weight, padding=self.kernel_size // 2, groups=self.groups
        )
        out = out.transpose(0, 1)
        return torch.relu(self.fc1(out.squeeze(0)))


class ProDataset(Dataset):
    def __init__(self, dataframe, data_path):
        self.names = dataframe['ID'].values
        self.sequences = dataframe['sequence'].values
        self.labels = dataframe['label'].values
        self.data_path = data_path


    def __getitem__(self, index):
        # index = self.getRandom()
        sequence_name = self.names[index]
        sequence = self.sequences[index]


        label = np.array(self.labels[index])
        data_path = self.data_path

        pssm_feature, hmm_feature, evo_feature = embedding(sequence_name, data_path)
        atom_features, seq_feature = get_atom_features(sequence_name, data_path)
        node_features = np.concatenate([pssm_feature, hmm_feature, atom_features, seq_feature], axis=1)
        graph = load_graph(sequence_name, data_path)
        graph = graph[:1000, :1000]

        return sequence_name, sequence, label[:1000], 0, node_features[:1000], graph, evo_feature

    def __len__(self):
        return len(self.labels)

class predict_ec(nn.Module):
    def __init__(self, hidden_dim):
        super(predict_ec, self).__init__()
        self.fc1 = nn.Linear(hidden_dim, 2*hidden_dim)
        self.fc2 = nn.Linear(2*hidden_dim, hidden_dim)
        self.fc3 = nn.Linear(hidden_dim, hidden_dim)
        self.fc4 = nn.Linear(hidden_dim, 1024)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))

        x = torch.mean(x, dim=0)
        x = torch.relu(self.fc4(x))
        return x


class SCOPE(nn.Module):
    def __init__(self, nlayers, nfeat, nhidden, nclass, dropout):
        super(SCOPE, self).__init__()

        self.gcn = deepGCN(nlayers=nlayers, nfeat=nfeat, nhidden=nhidden, nclass=nhidden,dropout=dropout,lamda=0.8,alpha=0.8,variant=True)
        # self.gcn = GCN(nlayers=nlayers, nfeat=nfeat, nhidden=nhidden, dropout=dropout)
        self.criterion = nn.CrossEntropyLoss()

        self.projection = nn.Linear(nhidden, nhidden//2)
        self.projection1 = nn.Linear(nhidden//2, nfeat)
        self.projection2 = nn.Linear(nfeat, nclass)
        self.act_fn =nn.ReLU()
        self.optimizer = torch.optim.Adam(self.parameters(), lr=LEARNING_RATE, betas=(0.9, 0.999))
        self.predict_ec = predict_ec(nhidden)
        self.gs_projection = nn.Linear(512, nclass)
        self.gs = Gaussis(512)

    def forward(self, x, adj, evo_fea):
        enz_feas = self.gcn(x.float(), adj, evo_fea)
        gs_feature = self.gs(enz_feas)
        inner_layer = self.act_fn(self.projection1(self.act_fn(self.projection(enz_feas))))
        output = self.projection2(inner_layer)
        ec_output = self.predict_ec(enz_feas)
        gs_output = self.gs_projection(gs_feature)
        return output, ec_output , gs_output




class deepGCN(nn.Module):
    def __init__(self, nlayers, nfeat, nhidden, nclass, dropout, lamda, alpha, variant):
        super(deepGCN, self).__init__()
        self.convs = nn.ModuleList()
        for _ in range(nlayers):
            self.convs.append(DEEP_GraphConvolution(nhidden, nhidden,variant=variant,residual=True))
        self.fcs = nn.ModuleList()
        self.fcs.append(nn.Linear(nfeat, nhidden))
        self.fcs.append(nn.Linear(nhidden, nclass))
        self.act_fn = nn.ReLU()
        self.dropout = dropout
        self.alpha = alpha
        self.lamda = lamda
        self.global_linear = nn.Linear(1024, 512)
        self.output_linear = nn.Linear(1024, 512)

    def forward(self, x, adj, evo_fea):
        _layers = []
        x = F.dropout(x, self.dropout, training=self.training)
        layer_inner = self.act_fn(self.fcs[0](x))
        _layers.append(layer_inner)
        for i,con in enumerate(self.convs):
            layer_inner = F.dropout(layer_inner, self.dropout, training=self.training)
            layer_inner = self.act_fn(con(layer_inner,adj,_layers[0],self.lamda,self.alpha,i+1))
        layer_inner = F.dropout(layer_inner, self.dropout, training=self.training)
        layer_inner = self.fcs[-1](layer_inner)
        # TODO 
        local_fea = layer_inner

        global_fea = F.dropout(evo_fea, self.dropout, training=self.training)
        # TODO 
        global_fea = self.act_fn(self.global_linear(global_fea))
        # TODO concatnate
        profeas = self.act_fn(self.output_linear(torch.cat([global_fea, local_fea], 1)))

        return profeas


class DEEP_GraphConvolution(nn.Module):
    def __init__(self, in_features, out_features, residual=False, variant=False):
        super(DEEP_GraphConvolution, self).__init__()
        self.variant = variant
        if self.variant:
            self.in_features = 2*in_features
        else:
            self.in_features = in_features

        self.out_features = out_features
        self.residual = residual
        self.weight = Parameter(torch.FloatTensor(self.in_features,self.out_features))
        self.reset_parameters()

    def reset_parameters(self):
        stdv = 1. / math.sqrt(self.out_features)
        self.weight.data.uniform_(-stdv, stdv)

    def forward(self, input, adj , h0 , lamda, alpha, l):
        theta = min(1, math.log(lamda/l+1))
        hi = torch.spmm(adj, input)
        if self.variant:
            support = torch.cat([hi,h0],1)
            r = (1-alpha)*hi+alpha*h0
        else:
            support = (1-alpha)*hi+alpha*h0
            r = support
        output = theta*torch.mm(support, self.weight)+(1-theta)*r
        if self.residual: # speed up convergence of the training process
            output = output+input
        return output
