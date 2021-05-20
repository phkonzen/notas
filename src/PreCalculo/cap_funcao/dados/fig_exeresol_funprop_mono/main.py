from sympy import *
init_printing()
var('x')

p = plot(abs(x),(x,-3,2),line_color="gray",show=False)
q = plot(abs(x+1),(x,-3,2),line_color="gray",show=False)
p.extend(q)
q = plot(-abs(x+1),(x,-3,2),line_color="blue",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_exeresol_prop_mono.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
fig.savefig('fig_exeresol_prop_mono.png', bbox_inches='tight')

