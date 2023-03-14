import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

x0 = 2
tol = 0.25

p = plot(x**2, (x,-1,2), line_color="blue", show=False)
q = plot(sqrt(x-2)+5, (x,2,3), line_color="blue", show=False)
p.extend(q)
q = plot(-1,(x,-1,3),line_color="none",show=False)
p.extend(q)
q = plot(7,(x,-1,3),line_color="none",show=False)
p.extend(q)
q = plot_implicit(y<sqrt(x-2)+5,(x,x0,x0+tol),(y,0,8),
                  line_color="0.85",show=False)
p.extend(q)
q = plot_implicit(x<(5-y)**2+2,(x,0,x0+tol),(y,sqrt(x0-2)+5,sqrt(x0+tol-2)+5),
                  line_color="0.85",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_lim_dir.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_yticks([])
ax.set_xticks([])
ax.grid()
ax.text(x0+tol-0.05,-0.45,"$\\leftarrow x$")
ax.plot([x0,x0],[0,sqrt(x0-2)+5-0.2],ls='--',color="red")
ax.plot([0,x0-0.05],[sqrt(x0-2)+5,sqrt(x0-2)+5],ls='--',color="red")
ax.text(x0-0.05,-0.45,"$x_0$")
ax.text(-0.15,sqrt(x0+tol-2)+5,"$\\downarrow$")
ax.text(-0.2,sqrt(x0-2)+5-0.1,"$L$")
ax.plot([x0],[x0**2],marker="o",markersize=5,markeredgecolor="red",markerfacecolor="white")
ax.plot([x0],[-(x0-2)**2+5],marker="o",markersize=5,markeredgecolor="red",markerfacecolor="white")
fig.savefig('fig_lim_dir.png', bbox_inches='tight')
