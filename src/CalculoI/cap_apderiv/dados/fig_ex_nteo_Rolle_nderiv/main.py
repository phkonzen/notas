#!/bin/python3

import numpy as np
from sympy import *
init_printing()
var('x',real=True)

p = plot(-abs(x-1)+1,(x,-0.5,2.5),line_color='blue',show=False)
# q = plot(4,(x,-2,3),line_color='none',show=False)
# p.extend(q)
# q = plot(-3,(x,-2,3),line_color='none',show=False)
# p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_ex_nteo_Rolle_nderiv.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid('on')
ax.set_xticks([0,1,2])
ax.set_yticks([0,1])
ax.plot([0],[0],marker="o",color="blue")
ax.plot([2],[0],marker="o",color="blue")
ax.plot([1],[1],marker="o",color="red")

fig.savefig('fig_ex_nteo_Rolle_nderiv.png', bbox_inches="tight")






