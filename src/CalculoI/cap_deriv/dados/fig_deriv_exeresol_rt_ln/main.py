from sympy import *
var('x,y', real=True)

p = plot(log(x), (x,0.07,4), line_color="blue", show=False)
q = plot(x-1,(x,0.1,2.5),line_color="red",show=False)
p.extend(q)
q = plot(-1,(x,-1,4),line_color="none",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_deriv_exeresol_rt_ln.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.plot([1],[0],marker="o",markersize=4,color="red")
fig.savefig('fig_deriv_exeresol_rt_ln.png', bbox_inches='tight')
