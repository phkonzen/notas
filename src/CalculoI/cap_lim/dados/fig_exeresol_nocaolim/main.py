import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 9,
     "font.sans-serif": "Computer Modern Roman",
     "text.latex.preamble": r"\usepackage{amsmath} \usepackage{amssymb}",
     "figure.figsize": [2.75, 2.75],
     "figure.dpi": 300
     })

var('x', real=True)

p = plot(-1.5, (x,-3,3), line_color="none", show=False)
q = plot(3.5, (x,-3,3),line_color="none",show=False)
p.extend(q)
p.xlabel = ''
p.ylabel = ''

p.save('fig.svg')
fig = p._backend.fig
ax = fig.axes[0]

ax.set_aspect('equal')
ax.grid()
ax.set_xticks([-3, -2, -1, 1, 2, 3])


ax.plot([-3,-2],[-1,1],color="blue")
ax.plot([-2,-1],[1,1],color="blue")
ax.plot([-1,1],[1,2],color="blue")
ax.plot([1,3],[1,3],color="blue")
ax.plot([-1],[1],marker='o', markersize=4,
        markeredgecolor="blue", markerfacecolor="white")
ax.plot([-1],[2],marker='o', markersize=4,
        markeredgecolor="blue", markerfacecolor="blue")
ax.plot([1],[2],marker='o', markersize=4,
        markeredgecolor="blue", markerfacecolor="white")
ax.plot([1],[1],marker='o', markersize=4,
        markeredgecolor="blue", markerfacecolor="blue")

ax.text(3.1, 0.15, '$x$')
ax.text(0.125, 3.5, '$y$')

fig.savefig('fig.png', bbox_inches='tight')
