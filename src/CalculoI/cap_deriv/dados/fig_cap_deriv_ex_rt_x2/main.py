from sympy import *
var('x,y', real=True)

x0 = 1

p = plot(x**2, (x,-1,3), line_color="blue", show=False)
q = plot(-1,(x,-1,3),line_color="none",show=False)
p.extend(q)
q = plot(2*x-1,(x,-1,3),line_color="red",show=False)
p.extend(q)
q = plot(3*x-2,(x,-1,3),line_color="green",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_cap_deriv_ex_rt_x2.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_ylim((-2,6))
ax.plot([x0],[x0**2],marker="o",markersize=4,color="red")
ax.plot([2],[4],marker="o",markersize=4,color="green")
ax.text(1.75,5.1,"$y=x^2$")
ax.text(2.52,5.4,"$y=3x-2$")
ax.text(2.52,3.75,"$y=2x-1$")
fig.savefig('fig_cap_deriv_ex_rt_x2.png', bbox_inches='tight')
