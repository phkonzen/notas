from sympy import *
var('x',real=True)

p = plot(log(x),(x,0.001,5),line_color='blue',show=False)
q = plot(0,(x,-1,5),line_color='none',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_ex_lim_assvert_lnx.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_ylim((-4,5))
ax.plot([0,0],[-4,5],ls="--",color="red",lw=2)
fig.savefig('fig_ex_lim_assvert_lnx.png', bbox_inches='tight')
