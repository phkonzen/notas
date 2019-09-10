from sympy import *
var('x,y', real=True)

p = plot(abs(x), (x,-3,3), line_color="blue", show=False)
q = plot(-2,(x,-3,3),line_color="none",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_deriv_ex_ffl_absx.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.plot([0],[0],marker="o",markersize=3,color="blue")
ax.plot([-3,0],[-1,-1],color="red")
ax.plot([0,3],[1,1],color="red")
ax.plot([0],[-1],marker="o",markersize=4,
        markerfacecolor="white",markeredgecolor="red",zorder=5)
ax.plot([0],[1],marker="o",markersize=4,
        markerfacecolor="white",markeredgecolor="red",zorder=5)
ax.text(-2.1,2.1,"$f(x) = |x|$", fontsize=12)
ax.text(2.1,1.1,"$f'(x)$", fontsize=12)
fig.savefig('fig_deriv_ex_ffl_absx.png', bbox_inches='tight')
