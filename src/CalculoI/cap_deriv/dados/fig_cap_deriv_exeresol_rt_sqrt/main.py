from sympy import *
var('x,y', real=True)

x0 = 4

p = plot(sqrt(x), (x,0,8), line_color="blue", show=False)
q = plot(-1,(x,-1,8),line_color="none",show=False)
p.extend(q)
q = plot(1/4*x+1,(x,-0.5,7),line_color="red",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_cap_deriv_exeresol_rt_sqrt.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.plot([x0],[sqrt(x0)],marker="o",markersize=4,color="red")
#ax.plot([2],[4],marker="o",markersize=4,color="green")
#ax.text(1.75,5.1,"$y=x^2$")
#ax.text(2.52,5.4,"$y=3x-2$")
#ax.text(2.52,3.75,"$y=2x-1$")
fig.savefig('fig_cap_deriv_exeresol_rt_sqrt.png', bbox_inches='tight')
