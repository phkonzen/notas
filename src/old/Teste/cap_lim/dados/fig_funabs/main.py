from sympy import *
var('x', real=True)

p = plot(abs(x), (x,-3,3), line_color="blue", show=False)
q = plot(-1,(x,-3,3),line_color="none",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_cap_funcao_funabs.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.text(2,2.75,"$y=|x|$",fontsize=12)
fig.savefig('fig.png', bbox_inches='tight')
