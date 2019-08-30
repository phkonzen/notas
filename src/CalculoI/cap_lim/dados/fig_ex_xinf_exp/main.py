from sympy import *
var('x',real=True)

p = plot(exp(x),(x,-5,2),line_color='blue',show=False)
q = plot(-1,(x,-5,2),line_color='none',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_ex_xinf_exp.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.plot([-5,2],[0,0],ls='--',color='red')
ax.text(1,6.1,"$y = e^x$",fontsize=12)
fig.savefig('fig_ex_xinf_exp.png', bbox_inches='tight')
