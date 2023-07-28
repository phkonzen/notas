import torch
import numpy as np

# load model
model = torch.load('model.pt')

# load test data
X_test = torch.from_numpy(np.load('x_test.npy')).type(torch.float32)
Y_test = torch.from_numpy(np.load('y_test.npy')).type(torch.float32)

# model estimates
Y_est = model(X_test)

# error
print(torch.norm(Y_est - Y_test)/torch.norm(Y_test))

