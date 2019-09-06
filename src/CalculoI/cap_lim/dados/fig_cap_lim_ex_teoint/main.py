from sympy import *
var('x', real=True)

p = plot(x**3-x-1, (x,-1,3), line_color="blue", show=False)
#q = plot(-1,(x,-1,3),line_color="none",show=False)
#p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_cap_lim_ex_teoint.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_ylim((-1.5,7))
ax.plot([0],[-1],marker="o",markersize=4,color="red")
ax.plot([2],[5],marker="o",markersize=4,color="red")
fig.savefig('fig_cap_lim_ex_teoint.png', bbox_inches='tight')
