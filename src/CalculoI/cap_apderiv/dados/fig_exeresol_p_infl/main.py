#!/bin/python3

import numpy as np
from sympy import *
init_printing()
var('x',real=True)

p = plot(x**3,(x,-1,1),line_color='blue',show=False)
#q = plot(,(x,-0.5,1),line_color='blue',show=False)
#p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$f(x)$'
p.save('fig_exeresol_p_infl.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid('on')
ax.plot([-1],[-1],marker='o',color='red')
ax.plot([0],[0],marker='o',color='blue')
ax.plot([1],[1],marker='o',color='red')
fig.savefig('fig_exeresol_p_infl.png')






