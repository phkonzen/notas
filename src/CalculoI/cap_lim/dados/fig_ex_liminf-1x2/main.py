from sympy import *
var('x,y', real=True)

f = lambda x: -1/(x+1)**2

p = plot(f(x), (x,-3,-1-1e-5), line_color="blue", show=False)
q = plot(f(x), (x,-1+1e-5,1), line_color="blue", show=False)
p.extend(q)
q = plot(2, (x,-3,1), line_color="none", show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_ex_liminf-1x2.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_ylim((-20,2))
ax.plot([-1,-1],[-20,2],ls="--",color="red",zorder=5)
fig.savefig('fig_ex_liminf-1x2.png', bbox_inches='tight')
