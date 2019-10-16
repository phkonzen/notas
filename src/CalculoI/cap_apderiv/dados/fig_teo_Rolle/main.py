#!/bin/python3

import numpy as np
from sympy import *
init_printing()
var('x',real=True)

a=0.5
b=2.5
f = -1.5*(x-a)*(x-b)+1
c = (a+b)/2

p = plot(f,(x,a,b),show=False)
q = plot(-0.5,(x,-0.5,3),line_color='none',show=False)
p.extend(q)
q = plot(3,(x,-0.5,3),line_color='none',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = ''
p.save('fig_teo_Rolle.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([0,a,c,b])
ax.set_xticklabels(["$0$","$a$","$c$","$b$"])
ax.set_yticks([0,f.subs(x,a),f.subs(x,c)])
ax.set_yticklabels(["$0$","$f(a) = f(b)$","$f(c)$"])
ax.plot([a,a],[0,f.subs(x,a)],ls="--",color="gray")
ax.plot([0,a],[f.subs(x,a),f.subs(x,a)],ls="--",color="gray")
ax.plot([b,b],[0,f.subs(x,b)],ls="--",color="gray")
ax.plot([a,b],[f.subs(x,b),f.subs(x,b)],ls="--",color="gray")
ax.plot([a],[f.subs(x,a)],marker="o",markersize=3,color="blue")

ax.text(c,f.subs(x,c)+0.1,"$f'(c)=0$",fontsize=12)
ax.plot([c,c],[0,f.subs(x,c)],ls="--",color="gray")
ax.plot([0,c],[f.subs(x,c),f.subs(x,c)],ls="--",color="gray")

ax.plot([c-0.5,c+0.5],[f.subs(x,c),f.subs(x,c)],color="red")
ax.plot([b],[f.subs(x,b)],marker="o",markersize=3,color="blue")
ax.plot([c],[f.subs(x,c)],marker="o",markersize=3,color="red")

fig.savefig('fig_teo_Rolle.png', bbox_inches="tight")





