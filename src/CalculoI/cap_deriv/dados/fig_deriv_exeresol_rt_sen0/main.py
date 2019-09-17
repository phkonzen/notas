from sympy import *
var('x,y', real=True)

f = sin(x)
x0 = 0

p = plot(f, (x,-pi,pi), line_color="blue", show=False)
q = plot(x,(x,-pi/3,pi/3),line_color="red",show=False)
p.extend(q)
q = plot(1.5,(x,-pi,pi),line_color="none",show=False)
p.extend(q)
q = plot(-1.5,(x,-pi,pi),line_color="none",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_deriv_exeresol_rt_sen0.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_xticks((-pi,-pi/2,0,pi/2,pi))
ax.set_xticklabels(["$-\\pi$","$-\\frac{\\pi}{2}$","$0$","$\\frac{\\pi}{2}$","$\\pi$"])
ax.plot([0],[0],marker="o",markersize=4,color="red")
ax.text(0.5,1.1,"$y=x$",fontsize=12)
ax.text(2*pi/3,1.05,"$y=\\operatorname{sen}\\,x$",fontsize=12)
fig.savefig('fig_deriv_exeresol_rt_sen0.png', bbox_inches='tight')
