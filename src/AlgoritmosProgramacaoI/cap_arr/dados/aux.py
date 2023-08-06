import numpy as np

def MatrizVetor(A, x):
    n,m = A.shape
    y = np.empty(n)
    for i in range(n):
        y[i] = 0.
        for j in range(m):
            y[i] += A[i,j]*x[j]
    return y

def MatrizMatriz(A, B):
    n,p = A.shape
    m = B.shape[1]
    C = np.empty((n,m))
    for i in range(n):
        for j in range(m):
            C[i,j] = 0.
            for k in range(p):
                C[i,j] += A[i,k]*B[k,j]
    return C

A = np.array([[1, -1, 2],
              [2,  1, 3],
              [0,  2, 1]])
B = np.array([[2, 0, 1],
              [1, 2, 0],
              [0, 2, 1]])
x = np.array([-1, 2, 1])
print(MatrizMatriz(A,B))

        

def bubbleSort(arr):
    arr = arr.copy()
    n = len(arr)
    for k in range(n-1):
        noUpdated = True
        for i in range(n-k-1):
            if not(arr[i] < arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                noUpdated = False
        if (noUpdated):
            break
    return arr

v = np.array([-1,1,0,4,3])
w = bubbleSort(v)
print(w)
