from sympy import *
var('x', real=True)

p = plot(-3, (x,-3,3), line_color="none", show=False)
q = plot(3,(x,-3,3),line_color="none",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_exeresol_nocaolim.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.plot([-3,-2],[-1,1],color="blue")
ax.plot([-2,-1],[1,1],color="blue")
ax.plot([-1,1],[1,2],color="blue")
ax.plot([1,3],[1,3],color="blue")
ax.plot([-1],[1],marker='o',markersize=4,markeredgecolor="blue",markerfacecolor="white")
ax.plot([-1],[2],marker='o',markersize=4,markeredgecolor="blue",markerfacecolor="blue")
ax.plot([1],[2],marker='o',markersize=4,markeredgecolor="blue",markerfacecolor="white")
ax.plot([1],[1],marker='o',markersize=4,markeredgecolor="blue",markerfacecolor="blue")
fig.savefig('fig_exeresol_nocaolim.png', bbox_inches='tight')
