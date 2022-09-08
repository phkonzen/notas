import matplotlib as plt
import numpy as np
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

p = plot(1.25, (x,-0.5,2.5), line_color='none', show=False)
q = plot((x-1)**3, (x,-0.25,2.25), show=False)
p.extend(q)
q = plot(x-1, (x,-0.35,2.35), show=False)
p.extend(q)
q = plot(-1.25, (x,-0.5,2.5), line_color='none', show=False)
p.extend(q)
q = plot_implicit(And(y < (x-1)**3, y > x-1),
                  (x,0,1), (y, -1, 0), line_color='gray', show=False)
p.extend(q)
q = plot_implicit(And(y > (x-1)**3, y < x-1),
                  (x,1,2), (y, 0, 2), line_color='gray', show=False)
p.extend(q)

p.ylabel = "$y$"
p.xlabel = "$x$"
p.save('fig.png')


fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_aspect("equal")
ax.set_xticks([0,1,2])
fig.savefig('fig.png', bbox_inches='tight')
