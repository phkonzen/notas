from sympy import *
from sympy.abc import *

# a
p = plot(x**(5/2),(x,-0.5,2),ylim=(-0.5,2),show=False,
         line_color="blue")
p.ylabel="$y$"
p.save('fig_exeresol_funpot_graf_a.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
fig.savefig('fig_exeresol_funpot_graf_a.png',bbox_inches='tight')

# b
p = plot(x**(5/3),(x,0,2),ylim=(-2,2),show=False,
         line_color="blue")
q = plot(-(-x)**(5/3),(x,-2,0),ylim=(-2,2),show=False,
        line_color="blue")
p.extend(q)
p.ylabel="$y$"
p.grid = True
p.save('fig_exeresol_funpot_graf_b.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
fig.savefig('fig_exeresol_funpot_graf_b.png',bbox_inches='tight')

