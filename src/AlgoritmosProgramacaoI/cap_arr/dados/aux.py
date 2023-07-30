import numpy as np
# vetores
v = np.array([1., 0, -2])
w = np.array([2., -1, 3])
# produto interno
vdw = np.sum(v*w)

print(vdw)

def emOrdem(x, y):
    return x < y

def bubbleSort(arr, emOrdem=emOrdem):
    arr = arr.copy()
    n = len(arr)
    for k in range(n-1):
        noUpdated = True
        for i in range(n-1):
            if not(emOrdem(arr[i], arr[i+1])):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                noUpdated = False
        if (noUpdated):
            break
    return arr

def argBubbleSort(arr):
    n = len(arr)
    ind = np.arange(n)
    for k in range(n-1):
        noUpdated = True
        for i in range(n-1):
            if (arr[ind[i]] > arr[ind[i+1]]):
                ind[i], ind[i+1] = ind[i+1], ind[i]
                noUpdated = False
        if (noUpdated):
            break
    return ind

v = np.array([-1,1,0,4,3])
w = bubbleSort(v)
print(w)
