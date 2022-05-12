import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })


var('x',real=True)

p = plot(x**2-x-2,(x,-2,3),show=False,
         line_color='blue')
p.ylabel="$f(x)$"
p.save('fig_funquad_concavidade_cima.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
fig.savefig('fig_funquad_concavidade_cima.png',bbox_inches='tight')


p = plot(-x**2+x+2,(x,-2,3),show=False,line_color='blue')
p.ylabel="$g(x)$"
p.save('fig_funquad_concavidade_baixo.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
fig.savefig('fig_funquad_concavidade_baixo.png',bbox_inches='tight')

