#!/bin/python3

import numpy as np
from sympy import *
init_printing()
var('x',real=True)

# a) f(x) = (x-1)^2+1
p = plot((x-1)**2+1,(x,0,1.5),show=False)
q = plot(-1,(x,-1,2),line_color='none',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$f(x) = x^2$'
p.save('fig_f.pdf')

fig = p._backend.fig
ax = fig.axes[0]
ax.plot([1],[1],marker='o',color='blue')
ax.plot([0],[2],marker='o',color='blue')
ax.plot([1.5,1.5],[0,0.5**2+1],ls='--',color='gray')
fig.savefig('fig_f.pdf')

# b) g(x) = \ln x
p = plot(log(x),(x,0.01,E),ylim=[-4,2],show=False)
q = plot(2,(x,-1,3),line_color='none',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$g(x) = \\ln\,x$'
p.save('fig_g.pdf')

fig = p._backend.fig
ax = fig.axes[0]
ax.plot([E],[1],marker='o',color='blue')
ax.plot([E,E],[0,1],ls='--',color='gray')
ax.plot([0,E],[1,1],ls='--',color='gray')
fig.savefig('fig_g.pdf')




