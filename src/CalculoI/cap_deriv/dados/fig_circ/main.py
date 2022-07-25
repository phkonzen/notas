import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

p = plot_implicit(Eq(x**2 + y**2, 1),
              (x, -1.5, 1.5), (y, -1.5, 1.5),
                  show = False)

p.ylabel = "$y$"
p.xlabel = "$x$"
p.save('fig.png')


fig = p._backend.fig
ax = fig.axes[0]
ax.set_aspect("equal", "box")
ax.text(0.5,1.,"$x^2 + y^2 = 1$")
fig.savefig('fig.png', bbox_inches='tight')
