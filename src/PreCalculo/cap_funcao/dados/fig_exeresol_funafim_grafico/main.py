import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })


var('x')

p=plot(-x-1,(x,-3,3),line_color='blue',show=False)
p.xlabel="$x$"
p.ylabel="$y$"
p.save('fig_exeresol_funafim_grafico.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.plot([-1],[0],color='red',marker='o',markersize=3)
ax.plot([1],[-2],color='red',marker='o',markersize=3)
ax.text(-1,0.1,'$(-1, 0)$')
ax.text(1,-1.9,'$(1, -2)$')
ax.text(2.2,-3,'$f(x)=-x-1$')
fig.savefig('fig_exeresol_funafim_grafico.png')
