def simpson(f,a,b):
  return (b-a)/6. * (f(a) + 4*f((a+b)/2.) + f(b))

def simad(f,a,b,tol=1e-8,hmin=1e-10):
  # intervalo calculado
  S = (a,a)
  # intervalo a ser calculado
  N = (a,b)
  # intervalo ativo
  A = N
  # aprox calculada em [a, b]
  J = 0.
  # aprox calculada em A
  JA = 0.
  # num f eval
  nfe = 0
  # info
  info = 0
  while (S != (a,b)):
    print(S,N,A)
    # tamanho do intervalo
    h = A[1]-A[0]
    while (h > hmin):
      J0 = simpson(f,A[0],A[1])
      JA = simpson(f,A[0],A[0]+h/2.)
      JA += simpson(f,A[0]+h/2.,A[1])
      nfe += 9
      # est erro
      est = np.fabs(J0-JA)/10.
      # criterio de parada
      if (est < tol*h/(b-a)):
        break
      else:
        A = (A[0],A[0]+h/2.)
        h = h/2.
        print("\t",S,N,A,h,est)
        if (h < hmin):
          print("Atencao! h < hmin !")
          info = -1
          break
    J += JA
    S = (a, A[1])
    N = (A[1], b)
    A = N
  return J, nfe, info
