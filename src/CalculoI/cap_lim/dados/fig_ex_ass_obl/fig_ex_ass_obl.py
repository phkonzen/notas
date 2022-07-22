import numpy as np
import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

p1 = plot((x**2-1)/(5*x-4),(x,-5,4/5-0.001),line_color='blue',show=False)
p2 = plot((x**2-1)/(5*x-4),(x,4/5+0.001,5),line_color='blue',show=False)
p = p1
p.extend(p2)
p.ylabel = '$y$'
p.save('fig.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_ylim((-2,2))
ax.plot([4/5,4/5],[-2,2],ls='--',color='gray')
xx = np.linspace(-5,5)
ax.plot(xx,1/5*xx+4/25,ls='--',color='red')
ax.text(1.5,1.1,'$\\displaystyle y = \\frac{x}{5}+\\frac{4}{25}$',
        bbox = dict(fc = "white", ec = "white"), color="red")
ax.text(1.5,-1.,'$\\displaystyle y = \\frac{x^2-1}{5x-4}$',
        bbox = dict(fc = "white", ec = "white"), color="blue")
fig.savefig('fig.png', bbox_inches='tight')
