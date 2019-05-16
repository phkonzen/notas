#!/bin/python3

import numpy as np
from sympy import *
init_printing()
var('x',real=True)

# f(x) = x^2
p = plot(x**2,(x,-2,2),ylim=[-1,4],show=False)
q = plot(-1,(x,-2,2),line_color='none',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$f(x) = x^2$'
p.save('fig_f.pdf')

fig = p._backend.fig
ax = fig.axes[0]
ax.plot([0],[0],marker='o',color='blue')
fig.savefig('fig_f.pdf')

# g(x) = -x^2
p = plot(-x**2,(x,-2,2),ylim=[-4,1],show=False)
q = plot(1,(x,-2,2),line_color='none',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$g(x) = -x^2$'
p.save('fig_g.pdf')

fig = p._backend.fig
ax = fig.axes[0]
ax.plot([0],[0],marker='o',color='blue')
fig.savefig('fig_g.pdf')

# h(x) = x^3
p = plot(x**3,(x,-2,2),ylim=[-4,4],show=False)
p.xlabel = '$x$'
p.ylabel = '$h(x) = x^3$'
p.save('fig_h.pdf')



