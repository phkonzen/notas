from sympy import *
var('x',real=True)

p = plot(-1/abs(x),(x,-5,-0.001),line_color='blue',show=False)
q = plot(-1/abs(x),(x,0.001,5),line_color='blue',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_ex_lim_assvert_1.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_ylim((-5,1))
ax.plot([0,0],[-5,5],ls="--",color="red",lw=2)
ax.text(0.1,0.5,"$x=0$")
fig.savefig('fig_ex_lim_assvert_1.png', bbox_inches='tight')
