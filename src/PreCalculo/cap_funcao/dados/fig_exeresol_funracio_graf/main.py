import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })

var('x')

p = plot((x-1)/(x-1),(x,-2,2),show=False)
q = plot(2,(x,-2,2),show=False,line_color='none')
p.extend(q)
q = plot(-1,(x,-2,2),show=False,line_color='none')
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_exeresol_funracio_graf.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.plot([1],[1],marker='o',markersize=6,markerfacecolor='white')
fig.savefig('fig_exeresol_funracio_graf.png', bbox_inches='tight')
