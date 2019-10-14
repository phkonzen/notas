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
p.ylabel = '$y$'
p.save('fig_f.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([0])
ax.set_yticks([])
ax.plot([0],[0],marker='o',color='red')
ax.text(1,4,"$f(x) = x^2$",fontsize=16)
fig.savefig('fig_f.png')

# g(x) = -x^2
p = plot(-x**2,(x,-2,2),ylim=[-4,1],show=False)
q = plot(1,(x,-2,2),line_color='none',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_g.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([0])
ax.set_yticks([])
ax.plot([0],[0],marker='o',color='red')
ax.text(0.5,-4,"$g(x) = -x^2$",fontsize=16)
fig.savefig('fig_g.png')

# h(x) = x^3
p = plot(x**3,(x,-2,2),ylim=[-4,4],show=False)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_h.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([0])
ax.set_yticks([])
ax.text(0.5,4,"$h(x) = x^3$",fontsize=16)
fig.savefig('fig_h.png')



