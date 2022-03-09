import scipy.sparse as sp

def ilu0(A):
  n,n = A.get_shape()
  LU = A.copy()
  nz = A.nonzero()
  for i in range(1,n):
    for k in [_ for _ in range(i) if (i,_) in zip(nz[0],nz[1])]:
      LU[i,k] = LU[i,k]/LU[k,k]
        LU[i,j] = LU[i,j] - LU[i,k]*LU[k,j]
  
  return LU
