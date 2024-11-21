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

x0 = 2
tol = 0.25

p = plot(x**2, (x,-1,2), line_color="blue", show=False)
q = plot(-(x-2)**2+5, (x,2,3), line_color="blue", show=False)
p.extend(q)
q = plot(-1,(x,-1,3),line_color="none",show=False)
p.extend(q)
q = plot(7,(x,-1,3),line_color="none",show=False)
p.extend(q)
q = plot_implicit(y<x**2,(x,x0-tol,x0),(y,0,8),
                  line_color="0.85",show=False)
p.extend(q)
q = plot_implicit(x<sqrt(y),(x,0,2),(y,(x0-tol)**2,x0**2),
                  line_color="0.85",show=False)
p.extend(q)
p.xlabel = ''
p.ylabel = ''
p.save('fig.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_yticks([])
ax.set_xticks([])
ax.grid()
ax.text(x0-tol-0.3,-0.45,"$x\\rightarrow$")
ax.plot([x0,x0],[0,x0**2-0.2],ls='--',color="red")
ax.plot([0,x0-0.05],[x0**2,x0**2],ls='--',color="red")
ax.text(x0-0.05,-0.45,"$x_0$")
ax.text(-0.15,(x0-tol)**2+0.2,"$\\uparrow$")
ax.text(-0.15,(x0-tol)**2-0.4,"$y$")
ax.text(-0.2,x0**2-0.1,"$L$")
ax.plot([x0],[x0**2],marker="o",markersize=6,markeredgecolor="red",markerfacecolor="white")
ax.plot([x0],[-(x0-2)**2+5],marker="o",markersize=6,markeredgecolor="red",markerfacecolor="white")
fig.savefig('fig.png', bbox_inches='tight')
