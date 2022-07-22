import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

f = lambda x: 1/(x-2)**2

x0=2
tol=0.25

p = plot(f(x), (x,-1,x0-1e-5), line_color="blue", show=False)
q = plot(f(x), (x,x0+1e-5,5), line_color="blue", show=False)
p.extend(q)
q = plot(-1, (x,-1,5), line_color="none", show=False)
p.extend(q)
q = plot_implicit(y<f(x),(x,x0-tol,x0+tol),(y,0,60),line_color="0.85",show=False)
p.extend(q)
q = plot_implicit(x<2+sqrt(1/y),(x,0,x0-1e-5),(y,f(x0-tol),60),
                  line_color="0.85",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$+\\infty$'
p.save('fig.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_ylim((-1,60))
ax.set_xticks([])
ax.set_yticks([])
ax.plot([x0,x0],[-1,60],ls="--",color="red")
ax.text(x0-0.1,-3.5,"$x_0$")
ax.text(x0-tol-0.2,-3.5,"$\\rightarrow$")
ax.text(x0+tol,-3.5,"$\\leftarrow$")
ax.text(-0.25,f(x0-tol)+0.5,"$\\uparrow$")
fig.savefig('fig.png', bbox_inches='tight')
