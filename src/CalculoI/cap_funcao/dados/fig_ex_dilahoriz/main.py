from sympy import *
init_printing()
var('x')

alpha = 0.5
f = lambda x: x**2-2*x+1

p = plot(f(x),(x,-2,4),line_color="gray",show=False)
q = plot(f(alpha*x),(x,-2,4),line_color="blue",show=False)
p.extend(q)
p.title = ("$\\alpha = %1.1f$" % alpha)
p.xlabel = '$x$'
p.ylabel = '$y$'
p[0].label = "$f(x) = x^3$"
p[1].label = "$f(\\alpha\\cdot x)$"
p.save('fig_ex_dilahoriz.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_yticks(range(0,9))
ax.legend(loc="upper right")
fig.savefig('fig_ex_dilahoriz.png', bbox_inches='tight')
