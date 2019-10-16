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
p.save('fig_ex_corol_mono_deriv.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid('on')
ax.set_xticks([pc[0],pc[1]])
ax.set_xticklabels(["$\\frac{4-\\sqrt{7}}{3}$","$\\frac{4+\\sqrt{7}}{3}$"])

ax.plot([pc[0],pc[0]],[0,f.subs(x,pc[0])],ls="--",color="gray")
ax.plot([pc[1],pc[1]],[0,f.subs(x,pc[1])],ls="--",color="gray")

ax.plot([pc[0]],[f.subs(x,pc[0])],marker="o",color="red")
ax.plot([pc[1]],[f.subs(x,pc[1])],marker="o",color="red")

fig.savefig('fig_ex_corol_mono_deriv.png', bbox_inches="tight")






