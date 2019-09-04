from sympy import *
var('x,y', real=True)

f = lambda x: 1/(x-2)**2

x0=2
tol=0.25

p = plot(f(x), (x,-1,x0-1e-5), line_color="blue", show=False)
q = plot(f(x), (x,x0+1e-5,5), line_color="blue", show=False)
p.extend(q)
q = plot(-1, (x,-1,5), line_color="none", show=False)
p.extend(q)
q = plot_implicit(y<f(x),(x,x0-tol,x0+tol),(y,0,60),line_color="gray",show=False)
p.extend(q)
q = plot_implicit(x<2+sqrt(1/y),(x,0,x0-1e-5),(y,f(x0-tol),60),
                  line_color="gray",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$+\\infty$'
p.save('fig_liminf.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_ylim((-1,60))
ax.set_xticks([])
ax.set_yticks([])
ax.plot([x0,x0],[-1,60],ls="--",color="red")
ax.text(x0-0.1,-3.5,"$x_0$",fontsize=12)
ax.text(x0-tol-0.1,-3,"$\\rightarrow$",fontsize=12)
ax.text(x0+tol-0.1,-3,"$\\leftarrow$",fontsize=12)
ax.text(-0.25,f(x0-tol),"$\\uparrow$",fontsize=12)
fig.savefig('fig_liminf.png', bbox_inches='tight')
