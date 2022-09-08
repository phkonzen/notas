import matplotlib as plt
import numpy as np
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

p = plot(2.25, (x,-0.5,pi+1.5), line_color='none', show=False)
q = plot(2*cos(x-1), (x,1,pi+1), show=False)
p.extend(q)
q = plot(-2.25, (x,-0.5,pi+1.5), line_color='none', show=False)
p.extend(q)
q = plot_implicit(y <= 2*cos(x-1),
                  (x,1,pi+1), (y, 0, 2), show=False)
p.extend(q)
q = plot_implicit(y >= 2*cos(x-1),
                  (x,pi/2+1,pi+1), (y, -2, 0), line_color='red', show=False)
p.extend(q)

p.ylabel = "$y$"
p.xlabel = "$x$"
p.save('fig.png')


fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_aspect("equal")
ax.set_xticks([1, np.pi/2+1, np.pi+1])
ax.set_xticklabels(["$a$", "b", "c"])
ax.set_yticklabels([])
ax.annotate("$\displaystyle\int_a^b f(x)\,dx$",
            xy = (1.5, 0.7), xytext = (2.5, 1.5),
            arrowprops=dict(arrowstyle='->', facecolor='black'),
            bbox = dict(fc='white',ec='none'))
ax.annotate("$\displaystyle\int_b^c f(x)\,dx$",
            xy = (3.5, -0.7), xytext = (1.5, -1.5),
            arrowprops=dict(arrowstyle='->', facecolor='black'),
            bbox = dict(fc='white',ec='none'))
fig.savefig('fig.png', bbox_inches='tight')
