#!/bin/python3

import numpy as np
from sympy import *
var('x')

gamma(S(3)/2)

beta(S(3)/2,S(1)/2)
pi/2
p = plot(gamma(x),(x,-3+0.001,-2-0.001),ylim=[-24,24],show=False)
q = plot(gamma(x),(x,-2+0.001,-1-0.001),ylim=[-24,24],show=False)
p.extend(q)
q = plot(gamma(x),(x,-1+0.001,-0.001),ylim=[-24,24],show=False)
p.extend(q)
q = plot(gamma(x),(x,0.001,5),ylim=[-24,24],show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$\Gamma(x)$'
p.save('fig.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.plot([-3,-3],[-24,24],ls='--',color='gray')
ax.plot([-2,-2],[-24,24],ls='--',color='gray')
ax.plot([-1,-1],[-24,24],ls='--',color='gray')
ax.plot([0,0],[-24,24],ls='--',color='gray')
fig.savefig('fig.png', bbox_inches="tight")

