import numpy as np

def lu(A):
    # num. de linhas
    n = A.shape[0]

    # inicialização
    U = A.copy()
    L = np.eye(n)

    print(f'\n0')
    print(f'L = \n{L}')
    print(f'U = \n{U}')

    # decomposição
    for i in range(n-1):
        for j in range(i+1,n):
            L[j,i] = U[j,i]/U[i,i]
            U[j,i:] -= L[j,i]*U[i,i:]

        print(f'{i+1}:')
        print(f'L = \n{L}')
        print(f'U = \n{U}')

    return L, U

# matriz
A = np.array([[-1., 2., -2.],
              [3., -4., 1.],
              [1., -5., 3.]])

L, U = lu(A)
