from sympy import *
var('x',real=True)

p1 = plot((x**3-2*x+1)/(2-3*x**3),(x,-5,real_root(2/3,3)-0.001),line_color='blue',show=False)
p2 = plot((x**3-2*x+1)/(2-3*x**3),(x,real_root(2/3,3)+0.001,5),line_color='blue',show=False)
p = p1
p.extend(p2)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_ex_ass_horizon.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_ylim((-1,1))
ax.plot([real_root(2/3,3),real_root(2/3,3)],[-1,1],ls='--',color='gray')
ax.plot([-5,5],[-1/3,-1/3],ls='--',color='red')
ax.text(3,-0.45,'$y=-\\frac{1}{3}$')
ax.text(real_root(2/3,3)+0.1,-0.75,'$x=\\sqrt[3]{2/3}$')
fig.savefig('fig_ex_ass_horizon.png', bbox_inches='tight')
