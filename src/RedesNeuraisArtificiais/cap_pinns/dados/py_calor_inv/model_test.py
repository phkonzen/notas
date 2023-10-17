import torch
import numpy as np
import matplotlib.pyplot as plt

# load model
model = torch.load('model.pt')

# load test data
X_test = torch.from_numpy(np.load('x_test.npy')).type(torch.float32)
Y_test = torch.from_numpy(np.load('y_test.npy')).type(torch.float32)

# model estimates
Y_est = model(X_test)

# error
print(torch.norm(Y_est - Y_test)/torch.norm(Y_test))

# gráfico de calibração
plt.plot([0,1],[0,1],ls='--',color='gray')
plt.plot(Y_test[:,0], Y_est[:,0].detach(),
         ls='', marker='o', color='blue')
plt.plot(Y_test[:,1], Y_est[:,1].detach(),
         ls='', marker='o', color='red')
plt.grid()
plt.show()
