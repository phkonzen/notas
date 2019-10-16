#!/bin/python3

import numpy as np
from sympy import *
init_printing()
var('x',real=True)

p = plot((x+1)**2-1,(x,-2,1),line_color='blue',show=False)
#q = plot(,(x,-0.5,1),line_color='blue',show=False)
#p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$f(x)$'
p.save('fig_exeresol_f_diff.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid('on')
ax.plot([-2],[0],marker='o',color='blue')
ax.plot([-1],[-1],marker='o',color='red')
ax.plot([1],[3],marker='o',color='red')
fig.savefig('fig_exeresol_f_diff.png')






