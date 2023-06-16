import numpy as np

def lu(A):
    # num. de linhas
    n = A.shape[0]

    # inicialização
    U = A.copy()
    L = np.eye(n)

    # decomposição
    for i in range(n-1):
        for j in range(i+1,n):
            L[j,i] = U[j,i]/U[i,i]
            U[j,i:] -= L[j,i]*U[i,i:]

    return L, U

# matriz
A = np.array([[-1., 2., -2.],
              [3., -4., 1.],
              [1., -5., 3.]])

L, U = lu(A)
