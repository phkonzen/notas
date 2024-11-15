import numpy as np

def poliLagrange(xpts, ypts):
  # num. pts
  n = xpts.size
  # interp poli
  p = np.poly1d(0)
  for i in range(n):
    # Lagrange poli
    L = np.poly1d(1)
    for j in range(n):
      if (i != j):
        L *= np.poly1d([1, -xpts[j]])/(xpts[i]-xpts[j])
    p += ypts[i] * L
  return p



# exemplo
xpts = np.array([-1., 0, 1])
ypts = np.array([-1., 1, 1/2])


# interp poli
p = poliLagrange(xpts, ypts)
print(p)

# verificação
print(p(x))
