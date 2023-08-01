import numpy as np

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
