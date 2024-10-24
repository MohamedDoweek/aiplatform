# -*- coding: utf-8 -*-
"""ai platform

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NvinTs74NKNUZJnrWI-uUNFIr7RW-UnK
"""

import torch
import torch.nn as nn
import torch.optim as optim
import seaborn as sns
import matplotlib.pyplot as plt

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(3, 3)
        self.fc2 = nn.Linear(3, 3)
        self.fc3 = nn.Linear(3, 3)
        self.fc4 = nn.Linear(3, 1)

    def forward(self, x):
        x = torch.sigmoid(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        x = torch.tanh(self.fc4(x))
        return x

net = SimpleNN()

inputs = torch.rand(100, 3)

outputs = net(inputs).detach().numpy()

sns.lineplot(x=range(len(outputs)), y=outputs.flatten())
plt.title('Network Predictions Before Training')
plt.show()

optimizer = optim.SGD(net.parameters(), lr=0.01)
criterion = nn.MSELoss()

target_outputs = torch.rand(100, 1)

initial_predictions = net(inputs).detach().numpy()
sns.lineplot(x=range(len(initial_predictions)), y=initial_predictions.flatten())
plt.title('Initial Predictions Before Training')
plt.show()

epochs = 100
for epoch in range(epochs):
    predictions = net(inputs)
    loss = criterion(predictions, target_outputs)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f'Epoch [{epoch}/{epochs}], Loss: {loss.item():.4f}')

final_predictions = net(inputs).detach().numpy()

plt.figure(figsize=(10,5))

plt.subplot(1, 2, 1)
sns.lineplot(x=range(len(initial_predictions)), y=initial_predictions.flatten())
plt.title('Predictions Before Training')

plt.subplot(1, 2, 2)
sns.lineplot(x=range(len(final_predictions)), y=final_predictions.flatten())
plt.title('Predictions After Training')

plt.show()