from sympy import *
var('x,y', real=True)

p = plot(sqrt(x), (x,0,5), line_color="blue", show=False)
q = plot(1/(2*sqrt(x)),(x,0.001,5),line_color="red",show=False)
p.extend(q)
q = plot(-1,(x,-1,5),line_color="none",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_deriv_ex_ffl_sqrtx.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_ylim((-1,5))
ax.plot([0],[0],marker="o",markersize=3,color="blue")
ax.text(3.2,2.1,"$f(x) = \\sqrt{x}$", fontsize=12)
ax.text(3.1,0.5,"$f'(x) = \\frac{1}{2\sqrt{x}}$", fontsize=12)
fig.savefig('fig_deriv_ex_ffl_sqrtx.png', bbox_inches='tight')
