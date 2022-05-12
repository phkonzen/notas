import matplotlib.pyplot as plt
from sympy import *
from sympy.abc import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })

p = plot(1/x,(x,-4,4),ylim=(-4,4),show=False,
         line_color="blue")
p[0].label="$y=1/x$"
p.legend = True
p.ylabel="$y$"
p.save('fig_funpot_negativo_impar.png')
fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
fig.savefig('fig_funpot_negativo_impar.png',bbox_inches='tight')


p = plot(1/x**2,(x,-4,4),ylim=(-4,4),show=False,
         line_color="blue")
p[0].label="$y=1/x^2$"
p.legend = True
p.ylabel="$y$"
p.save('fig_funpot_negativo_par.png')
fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
fig.savefig('fig_funpot_negativo_par.png',bbox_inches='tight')
