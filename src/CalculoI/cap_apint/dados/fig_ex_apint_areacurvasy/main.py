import matplotlib as plt
import numpy as np
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

p = plot(-3, (x, 0, 5), line_color='none', show=False)
q = plot_implicit(Eq(x, y**2), (x, 0, 5), (y, -3,3),
                  adaptive=False, points=1000, show=False)
p.extend(q)
q = plot(2-x, (x, 0, 5), line_color='blue', show=False)
p.extend(q)
q = plot_implicit(And(x>y**2, x<2-y), (x, 0, 4), (y, -2, 1),
                  line_color='gray', show=False)
p.extend(q)


p.ylabel = "$y$"
p.xlabel = "$x$"
p.save('fig.png')


fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_aspect("equal")
fig.savefig('fig.png', bbox_inches='tight')
