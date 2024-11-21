import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12,
     "font.sans-serif": "Computer Modern Roman",
     "text.latex.preamble": r"\usepackage{amsmath} \usepackage{amssymb}",
     "figure.figsize": [4, 4],
     "figure.dpi": 300
     })

var('x',real=True)

f = lambda x: (x+1)*(x-1)*(x-2)/((x-1)*(x-2))
p = plot(f(x),(x,-2,3),show=False,line_color="blue")
p.xlabel = ''
p.ylabel = ''
p.save('fig.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid("on")
ax.grid(True)
ax.text(3.1, -0.5, '$x$')
ax.text(0.1, 4.1, '$y$')
ax.plot([1,1],[0,2],ls='--',color='gray')
ax.plot([0,1],[2,2],ls='--',color='gray')
ax.plot([2,2],[0,3],ls='--',color='gray')
ax.plot([0,2],[3,3],ls='--',color='gray')
ax.plot([1],[2],marker='o',markersize=6,markeredgecolor="blue",markerfacecolor="white")
ax.plot([2],[3],marker='o', markersize=6,markeredgecolor="blue", markerfacecolor="white")
fig.savefig('fig.png', bbox_inches='tight')

