import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

p = plot_implicit(Eq((x**2 + y**2)**2, (x**2 - y**2)),
              (x, -1.5, 1.5), (y, -1, 1),
                  show = False)

p.ylabel = "$y$"
p.xlabel = "$x$"
p.save('fig.png')


fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_aspect("equal")
ax.text(0.25,0.5,"$(x^2 + y^2)^2 = x^2 - y^2$",
        bbox = dict(fc = "white", ec = "white"))
fig.savefig('fig.png', bbox_inches='tight')
