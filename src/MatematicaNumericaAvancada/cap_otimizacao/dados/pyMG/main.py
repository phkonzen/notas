import numpy as np
import numpy.linalg as npla
import scipy.optimize as spopt

# fun obj
def fun(x):
  '''
  Função de Rosenbrock
  '''
  return sum(100.*(x[1:]-x[:-1]**2.)**2. + (1.-x[:-1])**2.)

# gradiente da fun
def grad(x):
  xm = x[1:-1]
  xm_m1 = x[:-2]
  xm_p1 = x[2:]
  der = np.zeros_like(x)
  der[1:-1] = 200*(xm-xm_m1**2) - 400*(xm_p1 - xm**2)*xm - 2*(1-xm)
  der[0] = -400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0])
  der[-1] = 200*(x[-1]-x[-2]**2)
  
  return der

# problem dimension
n = 2

# num max iters
maxiter = 100000
# tolerancia
tol = 1e-10

# aprox. inicial
x = np.zeros(n)

siga = [x]
for k in range(maxiter):
  # direcao descendente
  d = -grad(x)

  # pesquisa linear
  alpha = spopt.line_search(fun, grad, x, d)[0]

  # atualizacao
  x = x + alpha * d

  nad = npla.norm(alpha * d)
  nfun = npla.norm(fun(x))

  if ((k+1) % 10 == 0):
    print(f"{k+1}: {alpha:1.2e} {nad:1.2e} {nfun:1.2e}")
    siga.append(x)

  if ((nfun < tol) or np.isnan(nfun)):
    break
