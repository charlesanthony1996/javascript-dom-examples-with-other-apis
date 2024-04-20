import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np


#Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
data = pd.read_csv(url, sep = ';')


data['quality'].value_counts()

mapping = {3:0, 4:1, 5:2, 6:3, 7:4, 8:5}
data_mapped = data

data_mapped['quality'] = data_mapped['quality'].map(mapping)
print(data_mapped)

x =data_mapped.drop('quality', axis =1)
y = data_mapped['quality'].values

print(y)

# Dataset Class

class WineDataset(Dataset):
    def __init__(self, features, labels):
        self.features = features
        self.labels = labels
        
        def __len__(self):
            return len(self.labels)
        
        def __getitem__(self, idx):
            return self.features[idx], self.label[idx]



# Nerual Network

class NeuralNet(nn.Module):
    def __init__(self, input_size, num_classes):
        super(NueralNet, self).__init__()
        
   
        self.fc1 = nn.Linear(input_size, 5)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(5, num_classes)
        
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out


x_train, x_tes, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 42)

x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size = 0.22, random_state = 42)


train_dataset = WineDataset(torch.FloatTensor(x_train), torch.LongTensor(y_train))
val_dataset = WineDataset(torch.FloatTensor(x_val), torch.LongTensor(y_val))
test_dataset = WineDataset(torch.FloatRTensor(x_test), torch.LongTensor(y_test))