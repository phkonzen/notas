from __future__ import division
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

#fun obj
f = lambda x: 3*np.sin(2*np.pi*x)

#intervalo
x0=1/4
x1=3/4

#interp
pif = interpolate.interp1d([x0,x1],[f(x0),f(x1)])

#grafico
xpts = np.linspace(x0,x1)
plt.plot(xpts,f(xpts),color="red",label="$f$")
plt.plot([x0,x1],[f(x0),f(x1)],
         color="red",linestyle="",
         marker="o",label="pts")
plt.plot(xpts,pif(xpts),
         color="blue",label=r"$\pi f$")
plt.grid("on")
plt.xlabel(r"$x$",fontsize=20)
plt.ylim((-3.5,3.5))
plt.legend(numpoints=1)
plt.show()
