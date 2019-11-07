#!/bin/python3

import numpy as np
from sympy import *
from sympy import plot_implicit
import matplotlib.patches as patches
init_printing()
var('x,y',real=True)

f = (x-0.5)**3 - 4*(x-0.5)**2 + 3*(x-0.5)+1 + 2.5

# pts criticos
pc = solve(f.diff())

p = plot(f,(x,0.5,3.25),line_color='blue',show=False)
q = plot(-0.5,(x,-0.5,3.75),line_color='none',show=False)
p.extend(q)
q = plot(5,(x,-0.5,3.75),line_color='none',show=False)
p.extend(q)
q = plot_implicit(y <= f, (x,0.5,3.25), (y,0,5), show=False,
                  line_color="gray")
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_geointdef.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid('on')
ax.set_xticks([0.5,3.25])
ax.set_xticklabels(["$a$","$b$"])
ax.set_yticks([float(f.subs(x,0.5)),float(f.subs(x,3.25))])
ax.set_yticklabels([])

ax.text(3.25,2.5,"$y=f(x)$")

ax.text(1.5,1.25,"$\\int_a^b f(x)\\,dx$",fontsize=14)

fig.savefig('fig_geointdef.png', bbox_inches="tight")






