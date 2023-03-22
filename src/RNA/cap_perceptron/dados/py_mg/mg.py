import torch

class mg():

    # inicializa
    def __init__(self, X, y, model, lr):        
        # dados de treinamento
        self.X = X
        self.y = y

        # modelo
        self.model = model

        # taxa de aprendizagem
        self.lr = lr

        # dimensões
        self.nin = model['weights'].size(0)
        self.ns = X_train.size(0)

        # gradientes
        self.dedw = torch.empty((nin, 1))
        self.dedb = torch.empty((1))

    # computa os gradientes
    def backward(self):
        # estou aqui!
        
