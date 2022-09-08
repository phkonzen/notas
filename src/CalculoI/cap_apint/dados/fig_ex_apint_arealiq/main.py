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
q = plot((x-1)**3, (x,0,2), show=False)
p.extend(q)
q = plot(-1.25, (x,-0.5,2.5), line_color='none', show=False)
p.extend(q)
q = plot_implicit(y >= (x-1)**3,
                  (x,0,1), (y, -1, 0), line_color='red', show=False)
p.extend(q)
q = plot_implicit(y <= (x-1)**3,
                  (x,1,2), (y, 0, 2), line_color='blue', show=False)
p.extend(q)

p.ylabel = "$y$"
p.xlabel = "$x$"
p.save('fig.png')


fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_aspect("equal")
ax.set_xticks([0,1,2])
ax.text(0.4,0.75,'$f(x)=(x-1)^3$',
        bbox=dict(fc='white',ec='none'))
fig.savefig('fig.png', bbox_inches='tight')
