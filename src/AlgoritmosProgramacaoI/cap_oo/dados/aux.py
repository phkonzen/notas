import numpy as np
import matplotlib.pyplot as plt

class Triangulo:
    '''
    Classe Triangulo ABC.
    '''
    num_lados = 3
    def __init__(self, A, B, C):
        # vértices
        self.A = A
        self.B = B
        self.C = C
        # lados
        self.a = 0.
        self.b = 0.
        self.c = 0.

    def calcLados(self):
        self.a = np.sqrt((self.B[0]-self.C[0])**2\
                         + (self.B[1]-self.C[1])**2)
        self.b = np.sqrt((self.A[0]-self.C[0])**2\
                         + (self.A[1]-self.C[1])**2)
        self.c = np.sqrt((self.A[0]-self.B[0])**2\
                         + (self.A[1]-self.B[1])**2)

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot()
        # lados
        ax.plot([self.A[0], self.B[0]],
                [self.A[1], self.B[1]], marker='o', color='blue')
        ax.text((self.A[0]+self.B[0])/2,
                (self.A[1]+self.B[1])/2, 'c')
        ax.plot([self.B[0], self.C[0]],
                [self.B[1], self.C[1]], marker='o', color='blue')
        ax.text((self.B[0]+self.C[0])/2,
                (self.B[1]+self.C[1])/2, 'a')
        ax.plot([self.C[0], self.A[0]],
                [self.C[1], self.A[1]], marker='o', color='blue')
        ax.text((self.A[0]+self.C[0])/2,
                (self.A[1]+self.C[1])/2, 'b')
        # vertices
        ax.text(self.A[0], self.A[1], 'A')
        ax.text(self.B[0], self.B[1], 'B')
        ax.text(self.C[0], self.C[1], 'C')
        ax.grid()
        plt.show()

tria = Triangulo((0., 0.),
                 (2., 0.),
                 (1., 1.))
tria.plot()
        

    
