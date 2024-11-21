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

var('x,y', real=True)

p = plot(x, (x,-1,3), line_color="blue", show=False)
x0 = 2
tol = 0.25
q = plot_implicit(y<x,(x,x0-tol,x0+tol),(y,0,8),
                  line_color="0.85",show=False)
p.extend(q)
q = plot_implicit(x<y,(x,0,3),(y,(x0-tol),(x0+tol)),
                  line_color="0.85",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_yticks([])
ax.set_xticks([])
ax.grid()
ax.set_aspect("equal","box")
ax.text(x0-tol-0.3,-0.25,"$x\\rightarrow$")
ax.text(x0+tol,-0.25,"$\\leftarrow x$")
ax.text(x0-0.05,-0.25,"$x_0$")

ax.plot([x0,x0],[0,x0-0.1],ls='--',color="red")
ax.plot([0,x0-0.05],[x0,x0],ls='--',color="red")

ax.text(-0.2,x0-tol-0.1,"$\\uparrow$")
ax.text(-0.2,x0+tol,"$\\downarrow$")
ax.text(-0.3,x0-0.05,"$x_0$")
ax.plot([x0],[x0],marker="o",markersize=6,markeredgecolor="red",markerfacecolor="red")
ax.text(2.5+0.2,2.5,"$y=x$")
fig.savefig('fig.png', bbox_inches='tight')
