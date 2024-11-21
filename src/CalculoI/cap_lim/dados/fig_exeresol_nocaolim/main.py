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

var('x', real=True)

p = plot(-3, (x,-3,3), line_color="none", show=False)
q = plot(3,(x,-3,3),line_color="none",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.plot([-3,-2],[-1,1],color="blue")
ax.plot([-2,-1],[1,1],color="blue")
ax.plot([-1,1],[1,2],color="blue")
ax.plot([1,3],[1,3],color="blue")
ax.plot([-1],[1],marker='o', markersize=6,
        markeredgecolor="blue", markerfacecolor="white")
ax.plot([-1],[2],marker='o', markersize=6,
        markeredgecolor="blue", markerfacecolor="blue")
ax.plot([1],[2],marker='o', markersize=6,
        markeredgecolor="blue", markerfacecolor="white")
ax.plot([1],[1],marker='o', markersize=6,
        markeredgecolor="blue", markerfacecolor="blue")
fig.savefig('fig.png',
            bbox_inches='tight')
