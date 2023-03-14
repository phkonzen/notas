import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x',real=True)

p1 = plot(-3,(x,-2,4),line_color='none',show=False)
p2 = plot(3,(x,-2,4),line_color='none',show=False)
p = p1
p.extend(p2)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_exer_limgraf.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid('on')
ax.plot([-2,-1],[-2,-1],color='blue')
ax.plot([-1,1],[-1,-1],color='blue')
ax.plot([1,2],[-1,2],color='blue')
ax.plot([2,3],[2,1],color='blue')
ax.plot([3,4],[2,3],color='blue')
ax.plot([-1],[-1],marker='o',
        markeredgecolor='blue',markerfacecolor='white',markersize=6)
# ax.plot([1],[-1],marker='o',
#         markeredgecolor='blue',markerfacecolor='blue',markersize=6)
ax.plot([2],[2],marker='o',
        markeredgecolor='blue',markerfacecolor='white',markersize=6)
ax.plot([2],[1],marker='o',
        markeredgecolor='blue',markerfacecolor='blue',markersize=6)
ax.plot([3],[1],marker='o',
        markeredgecolor='blue',markerfacecolor='blue',markersize=6)
ax.plot([3],[2],marker='o',
        markeredgecolor='blue',markerfacecolor='white',markersize=6)
fig.savefig('fig_exer_limgraf.png', bbox_inches='tight')
