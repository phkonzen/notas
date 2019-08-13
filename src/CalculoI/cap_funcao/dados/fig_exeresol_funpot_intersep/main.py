from sympy import *
from sympy.abc import *

p = plot(1/x,(x,-2,-0.3),show=False,line_color='blue')
q = plot(1/x,(x,0.3,2),show=False,line_color='blue')
p.extend(q)
q = plot(x**(1/3),(x,0,2),show=False,line_color='red')
p.extend(q)
q = plot(-(-x)**(1/3),(x,-2,0),show=False,line_color='red')
p.extend(q)
p.ylabel="$y$"
p.save('fig_exeresol_funpot_intersep.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.plot([1],[1],marker='o',markersize=4,color='green')
ax.plot([-1],[-1],marker='o',markersize=4,color='green')
# ax.ylim((-2,2))
fig.savefig('fig_exeresol_funpot_intersep.png',bbox_inches='tight')

