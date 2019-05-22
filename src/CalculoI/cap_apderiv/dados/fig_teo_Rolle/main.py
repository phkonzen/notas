#!/bin/python3

import numpy as np
from sympy import *
init_printing()
var('x',real=True)

p = plot(-0.5*(x-1)*(x-3)*x**2,(x,1,3),show=False)
q = plot(-1,(x,-1,4),line_color='none',show=False)
q = plot(3,(x,-1,4),line_color='none',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$f(x)$'
p.save('fig_teo_Rolle.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_yticks([-1,2.42404,3])
ax.set_yticklabels(['','$f(c)$',''])
c=2.36603
ax.set_xticks([-1,1,c,3,4])
ax.set_xticklabels(['','$a$','$c$','$b$',''])
ax.plot([c,c],[0,2.42404],ls='--',color='gray')
ax.plot([0,c],[2.42404,2.42404],ls='--',color='gray')
ax.plot([c],[2.42404],marker='o',markersize=3,color='red')
ax.plot([1],[0],marker='o',markersize=3,color='blue')
ax.plot([3],[0],marker='o',markersize=3,color='blue')
ax.plot([c-0.5,c+0.5],[2.42404,2.42404],color='black')
ax.text(c,2.5,"$f'(c)=0$")
fig.savefig('fig_teo_Rolle.png')





