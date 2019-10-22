#!/bin/python3

import numpy as np
from sympy import *
init_printing()
var('x',real=True)

f = Lambda(x, x**3/3-2*x**2+3*x+3)

p = plot(f(x),(x,-0.25,1),line_color='red',show=False)
q = plot(f(x),(x,1,3),line_color='blue',show=False)
p.extend(q)
q = plot(f(x),(x,3,4),line_color='red',show=False)
p.extend(q)
q = plot(6,(x,-0.5,4),line_color='none',show=False)
p.extend(q)
q = plot(-0.5,(x,-0.5,4),line_color='none',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_tder1.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid('on')
ax.set_xticks([0,1,3])
ax.set_xticklabels(["$0$","$c$","$d$"])
ax.set_yticks([f(1),f(3)])
ax.set_yticklabels(["$f(c)$","$f(d)$"])
ax.plot([1],[f(1)],marker="o",color="red")
ax.plot([3],[f(3)],marker="o",color="red")
ax.text(0.4,f(0.4)+0.5,"$f'>0$",fontsize=12)
ax.text(2,f(0.4)+0.5,"$f'<0$",fontsize=12)
ax.text(3.25,f(0.4)+0.5,"$f'>0$",fontsize=12)

fig.savefig('fig_tder1.png', bbox_inches="tight")






