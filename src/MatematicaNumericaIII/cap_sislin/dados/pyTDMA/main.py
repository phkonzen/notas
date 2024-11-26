import numpy as np

def TDMA(a,b,c,d):
    n = b.size
    for i in np.arange(1,n):
      w = a[i]/b[i-1]
      b[i] = b[i] - w*c[i-1]
      d[i] = d[i] - w*d[i-1]
    x = np.empty(n)
    x[n-1] = d[n-1]/b[n-1]
    for i in np.arange(n-2,-1,-1):
      x[i] = (d[i] - c[i]*x[i+1])/b[i]
    return x
