import torch

class NN(torch.nn.Module):
    def __init__(self):
        super(NN, self).__init__()
        self.layer1 = torch.nn.Linear(10, 64)
        self.layer2 = torch.nn.Linear(64, 128)
        self.layer3 = torch.nn.Linear(128, 1)

    def forward(self, x):
        x = self.layer1(x)
        x = torch.nn.functional.relu(x)
        x = torch.nn.functional.dropout(x, 0.25)  # dropout 
        x = self.layer2(x)
        x = torch.nn.functional.relu(x)
        x = torch.nn.functional.dropout(x, 0.25)
        x = self.layer3(x)
        x = torch.sigmoid(x)
        return x



