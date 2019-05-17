#!/bin/python3

import numpy as np
from sympy import *
init_printing()
var('x',real=True)

p = plot(-(x+1)**2-2,(x,-2,-0.5),line_color='blue',show=False)
q = plot(abs(x),(x,-0.5,1),line_color='blue',show=False)
p.extend(q)
q = plot((x-2)**3+2,(x,1,3),line_color='blue',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$f(x)$'
p.save('fig_f.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid('on')
ax.plot([-2],[-3],marker='o',color='blue')
ax.plot([-1],[-2],marker='o',color='blue')
ax.plot([-0.5],[-0.5**2-2],marker='o',color='blue',markerfacecolor='none')
ax.plot([-0.5],[0.5],marker='o',color='blue')
ax.plot([0],[0],marker='o',color='blue')
ax.plot([2],[2],marker='o',color='blue')
ax.plot([3],[3],marker='o',color='blue',markerfacecolor='none')
ax.plot([-0.5,-0.5],[-0.5**2-2,0.5],ls='--',color='gray')
ax.plot([0,-0.5],[-0.5**2-2,-0.5**2-2],ls='--',color='gray')
ax.plot([0,-0.5],[0.5,0.5],ls='--',color='gray')
fig.savefig('fig_f.png')






