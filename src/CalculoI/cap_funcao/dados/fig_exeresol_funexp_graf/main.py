from sympy import *
init_printing()
var('x')

# f_1 -> f_2
p = plot(exp(-x),(x,-2,5),line_color="gray",show=False)
q = plot(exp(-(x-1/2)),(x,-2,5),line_color="blue",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p[0].label = "$f_1(x) = e^{-x}$"
p[1].label = "$f_2(x) = e^{-(x-\\frac{1}{2})}$"
p.save('fig_exeresol_funexp_graf_1.png')

fig = p._backend.fig
ax = fig.axes[0]
# ax.set_yticks(range(-8,9))
ax.grid()
ax.legend(loc="upper right")
fig.savefig('fig_exeresol_funexp_graf_1.png', bbox_inches='tight')

# f_2 -> f_3
p = plot(exp(-(x-1/2)),(x,-1,5),line_color="gray",show=False)
q = plot(exp(-2*(x-1/2)),(x,-1,5),line_color="blue",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p[0].label = "$f_1(x) = e^{-(x-\\frac{1}{2})}$"
p[1].label = "$f_2(x) = e^{-2(x-\\frac{1}{2})}$"
p.save('fig_exeresol_funexp_graf_2.png')

fig = p._backend.fig
ax = fig.axes[0]
# ax.set_yticks(range(-8,9))
ax.grid()
ax.legend(loc="upper right")
fig.savefig('fig_exeresol_funexp_graf_2.png', bbox_inches='tight')

# f_3 -> f_4
p = plot(exp(-2*(x-1/2)),(x,-1,5),line_color="gray",show=False)
q = plot(exp(-2*(x-1/2))-1,(x,-1,5),line_color="blue",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p[0].label = "$f_1(x) = e^{-2(x-\\frac{1}{2})}$"
p[1].label = "$f_2(x) = e^{-2(x-\\frac{1}{2})}-1$"
p.save('fig_exeresol_funexp_graf_3.png')

fig = p._backend.fig
ax = fig.axes[0]
# ax.set_yticks(range(-8,9))
ax.grid()
ax.legend(loc="upper right")
fig.savefig('fig_exeresol_funexp_graf_3.png', bbox_inches='tight')

