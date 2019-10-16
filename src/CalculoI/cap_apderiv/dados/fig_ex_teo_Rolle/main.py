#!/bin/python3

import numpy as np
from sympy import *
init_printing()
var('x',real=True)

f = x**3 - 4*x**2 + 3*x+1

# pts criticos
pc = solve(f.diff())

p = plot(f,(x,-0.5,3.5),line_color='blue',show=False)
# q = plot(4,(x,-2,3),line_color='none',show=False)
# p.extend(q)
# q = plot(-3,(x,-2,3),line_color='none',show=False)
# p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_ex_teo_Rolle.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid('on')
ax.set_xticks([0,1,2,3])
ax.plot([0],[1],marker="o",color="blue")
ax.plot([1],[1],marker="o",color="blue")
ax.plot([3],[1],marker="o",color="blue")

ax.plot([pc[0]],[f.subs(x,pc[0])],marker="o",color="red")
ax.plot([pc[1]],[f.subs(x,pc[1])],marker="o",color="red")
fig.savefig('fig_ex_teo_Rolle.png', bbox_inches="tight")






