from sympy import *
var('x',real=True)

f = lambda x: (x-2)*(x+2)**2/((x-1)*(x+1))

p = plot(f(x),(x,-5,-1-0.001),line_color='blue',show=False)
q = plot(f(x),(x,-1+0.001,1-0.001),line_color='blue',show=False)
p.extend(q)
q = plot(f(x),(x,1+0.001,5),line_color='blue',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_ex_lim_assvert_racio.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_ylim((-30,30))
ax.plot([-1,-1],[-30,30],ls="--",color="red",lw=2)
ax.plot([1,1],[-30,30],ls="--",color="red",lw=2)
fig.savefig('fig_ex_lim_assvert_racio.png', bbox_inches='tight')
