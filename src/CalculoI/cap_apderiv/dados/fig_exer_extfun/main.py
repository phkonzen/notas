#!/bin/python3

import numpy as np
from sympy import *
init_printing()
var('x',real=True)

f = x**5/5 - 5*x**3/3 + 4*x

p = plot(f,(x,-2,2.5),line_color='blue',show=False)
q = plot(4,(x,-2,3),line_color='none',show=False)
p.extend(q)
q = plot(-3,(x,-2,3),line_color='none',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_exer_extfun.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid('on')
ax.set_xticks([-2,-1,0,1,2,2.5,3])
ax.set_xticklabels(["$-2$","$-1$","$0$","$1$","$2$","$\\frac{5}{2}$","$3$"])
ax.plot([-2],[f.subs(x,-2)],marker="o",markersize=4,
        markeredgecolor="blue",markerfacecolor="blue")
ax.plot([-1],[f.subs(x,-1)],marker="o",markersize=4,
        markeredgecolor="blue",markerfacecolor="blue")
ax.plot([0],[f.subs(x,0)],marker="o",markersize=4,
        markeredgecolor="blue",markerfacecolor="blue")
ax.plot([1],[f.subs(x,1)],marker="o",markersize=4,
        markeredgecolor="blue",markerfacecolor="blue")
ax.plot([2],[f.subs(x,2)],marker="o",markersize=4,
        markeredgecolor="blue",markerfacecolor="blue")
ax.plot([2.5],[f.subs(x,2.5)],marker="o",markersize=4,
        markeredgecolor="blue",markerfacecolor="blue")
fig.savefig('fig_exer_extfun.png')






