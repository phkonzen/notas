from __future__ import division
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

#fun obj
f = lambda x: 3*np.sin(2*np.pi*x)

#malha
n=5
l0=1/4
l1=3/4
xx = np.linspace(l0,l1,n)

#interp
pif = interpolate.interp1d(xx,f(xx))

#grafico
xpts = np.linspace(l0,l1)
plt.plot(xpts,f(xpts),color="red",label="$f$")
plt.plot(xx,f(xx),
         color="red",linestyle="",
         marker="o",label="pts")
plt.plot(xpts,pif(xpts),
         color="blue",label=r"$\pi f$")
plt.grid("on")
plt.xlabel(r"$x$",fontsize=20)
plt.ylim((-3.5,3.5))
plt.legend(numpoints=1)
plt.show()
