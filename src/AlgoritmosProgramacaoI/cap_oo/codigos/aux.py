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


class TrianguloIsosceles(Triangulo):
    def __init__(self,A,B,C):
        # vertices
        super().__init__(A,B,C)
        # lados
        self.a = self.b = self.c = 0.

    def setLados(self):
        self.a = np.sqrt((self.B[0] - self.C[0])**2\
                         + (self.B[1] - self.C[1])**2)
        self.b = np.sqrt((self.A[0] - self.C[0])**2\
                         + (self.A[1] - self.C[1])**2)
        self.c = np.sqrt((self.B[0] - self.A[0])**2\
                         + (self.B[1] - self.A[1])**2)
        assert(self.a == self.b)

tria = TrianguloIsosceles((1,0),
                          (3,0),
                          (2,1))
tria.plot()
tria.setLados()
        
        
