import numpy as np
import matplotlib.pyplot as plt

#fun obj
f = lambda x: 3*np.sin(2*np.pi*x)

#malha
n=11
xx=np.linspace(0,1,n)

#interp
xx1=np.linspace(0,1)
pif_vals = np.interp(xx1,xx,f(xx))

#grafico
plt.plot(xx1,f(xx1),color="red")
plt.plot(xx,f(xx),color="red",marker="o")
plt.plot(xx1,pif_vals,color="blue")
plt.grid("on")
plt.xlabel("$x$")
plt.xlabel("$x$")
plt.show()

