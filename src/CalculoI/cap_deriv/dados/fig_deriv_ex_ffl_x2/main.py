from sympy import *
var('x,y', real=True)

p = plot(x**2, (x,-3,3), line_color="blue", show=False)
q = plot(2*x,(x,-3,3),line_color="red",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_deriv_ex_ffl_x2.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.text(-2.4,6.5,"$f(x) = x^2$", fontsize=12)
ax.text(-2.9,-3.9,"$f'(x) = 2x$", fontsize=12)
fig.savefig('fig_deriv_ex_ffl_x2.png', bbox_inches='tight')
