from sympy import *
init_printing()
var('x')

# f_1 -> f_2
p = plot(x**3,(x,-2,3),ylim=[-8,8],line_color="gray",show=False)
q = plot((x-1)**3,(x,-2,3),line_color="blue",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p[0].label = "$f_1(x) = x^3$"
p[1].label = "$f_2(x) = (x-1)^3$"
p.save('fig_exeresol_opfun_graf_1.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_yticks(range(-8,9))
ax.grid()
ax.legend(loc="upper left")
fig.savefig('fig_exeresol_opfun_graf_1.png', bbox_inches='tight')

# f_2 -> f_3
p = plot((x-1)**3,(x,-2,3),ylim=[-8,8],line_color="gray",show=False)
q = plot(2*(x-1)**3,(x,-2,3),line_color="blue",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p[0].label = "$f_2(x) = (x-1)^3$"
p[1].label = "$f_3(x) = 2(x-1)^3$"
p.save('fig_exeresol_opfun_graf_2.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_yticks(range(-8,9))
ax.grid()
ax.legend(loc="upper left")
fig.savefig('fig_exeresol_opfun_graf_2.png', bbox_inches='tight')

# f_3-> f_4
p = plot(2*(x-1)**3,(x,-2,3),ylim=[-8,8],line_color="gray",show=False)
q = plot(2*(x-1)**3+1,(x,-2,3),line_color="blue",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p[0].label = "$f_3(x) = 2(x-1)^3$"
p[1].label = "$f_4(x) = 2(x-1)^3+1$"
p.save('fig_exeresol_opfun_graf_3.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_yticks(range(-8,9))
ax.grid()
ax.legend(loc="upper left")
fig.savefig('fig_exeresol_opfun_graf_3.png', bbox_inches='tight')
