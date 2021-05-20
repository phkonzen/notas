from sympy import *
init_printing()
var('x')

f = lambda x: x**2-2*x+2

p = plot(f(x),(x,-1,3),line_color="gray",show=False)
q = plot(-f(x),(x,-1,3),line_color="blue",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p[0].label = "$f(x) = x^2-2x+2$"
p[1].label = "$-f(x)$"
p.save('fig_ex_reflex.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_yticks(range(-5,6))
ax.legend(loc="upper right")
fig.savefig('fig_ex_reflex.png', bbox_inches='tight')
