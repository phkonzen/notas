from sympy import *
var('x,y', real=True)

p = plot(x, (x,-1,3), line_color="blue", show=False)
x0 = 2
tol = 0.25
q = plot_implicit(y<x,(x,x0-tol,x0+tol),(y,0,8),
                  line_color="gray",show=False)
p.extend(q)
q = plot_implicit(x<y,(x,0,3),(y,(x0-tol),(x0+tol)),
                  line_color="gray",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_lim_funid.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_yticks([])
ax.set_xticks([])
ax.grid()
ax.text(x0-tol-0.1,-0.2,"$x\\rightarrow$")
ax.text(x0+tol-0.1,-0.2,"$\\leftarrow x$")
ax.plot([x0,x0],[0,x0-0.1],ls='--',color="red")
ax.plot([0,x0-0.05],[x0,x0],ls='--',color="red")
ax.text(x0-0.05,-0.2,"$x_0$")
ax.text(-0.15,(x0-tol),"$\\uparrow$")
ax.text(-0.15,(x0+tol)-0.1,"$\\downarrow$")
ax.text(-0.125,x0-0.05,"$L$")
ax.plot([x0],[x0],marker="o",markersize=5,markeredgecolor="red",markerfacecolor="gray")
ax.text(2.5+0.125,2.5,"$y=x$")
fig.savefig('fig_lim_funid.png', bbox_inches='tight')
