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

var('x',real=True)

p1 = plot(-2, (x,-2,4),line_color='none',show=False)
p2 = plot(3 , (x,-2,4),line_color='none',show=False)
p = p1
p.extend(p2)
p.xlabel = ''
p.ylabel = ''

p.save('fig.svg')
fig = p._backend.fig
ax = fig.axes[0]

ax.set_aspect('equal')
ax.grid()
ax.set_xticks([-2, -1, 1, 2, 3, 4])


ax.plot([-2,-1],[-2,-1],color='blue')
ax.plot([-1,1],[-1,-1],color='blue')
ax.plot([1,2],[-1,2],color='blue')
ax.plot([2,3],[2,1],color='blue')
ax.plot([3,4],[2,3],color='blue')
ax.plot([-1],[-1],marker='o',
        markeredgecolor='blue',markerfacecolor='white',markersize=4)
# ax.plot([1],[-1],marker='o',
#         markeredgecolor='blue',markerfacecolor='blue',markersize=6)
ax.plot([2],[2],marker='o',
        markeredgecolor='blue',markerfacecolor='white',markersize=4)
ax.plot([2],[1],marker='o',
        markeredgecolor='blue',markerfacecolor='blue',markersize=4)
ax.plot([3],[1],marker='o',
        markeredgecolor='blue',markerfacecolor='blue',markersize=4)
ax.plot([3],[2],marker='o',
        markeredgecolor='blue',markerfacecolor='white',markersize=4)

ax.text(4.1, 0.15, '$x$')
ax.text(0.125, 3.25, '$y$')

fig.savefig('fig.png', bbox_inches='tight')
