#!/bin/python3

import numpy as np
from sympy import *
import numpy as np
init_printing()
var('x',real=True)

a=1
b=4
f = (x-1)*(x-3)+2
c = 5/2

p = plot(f,(x,a,b),show=False)
q = plot(-0.5,(x,-0.5,4.5),line_color='none',show=False)
p.extend(q)
q = plot(5.5,(x,-0.5,4.5),line_color='none',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = ''
p.save('fig_teo_valmed.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([0,a,c,b])
ax.set_xticklabels(["$0$","$a$","$c$","$b$"])
ax.set_yticks([0,f.subs(x,a),f.subs(x,b),f.subs(x,c)])
ax.set_yticklabels(["$0$","$f(a)$","f(b)","$f(c)$"])
ax.plot([a,a],[0,f.subs(x,a)],ls="--",color="gray")
ax.plot([0,a],[f.subs(x,a),f.subs(x,a)],ls="--",color="gray")
ax.plot([b,b],[0,f.subs(x,b)],ls="--",color="gray")
ax.plot([0,b],[f.subs(x,b),f.subs(x,b)],ls="--",color="gray")
ax.plot([a],[f.subs(x,a)],marker="o",markersize=3,color="blue")
ax.plot([b],[f.subs(x,b)],marker="o",markersize=3,color="blue")

ax.plot([c],[f.subs(x,c)],marker="o",markersize=3,color="red")
ax.plot([c,c],[0,f.subs(x,c)],ls="--",color="gray")
ax.plot([0,c],[f.subs(x,c),f.subs(x,c)],ls="--",color="gray")

xx = np.linspace(c-1.5,c+1.5)
yy = (xx - c) + f.subs(x,c)
ax.plot(xx,yy,color="red")

ax.plot([a,b],[f.subs(x,a),f.subs(x,b)],ls="--",color="blue")

fig.savefig('fig_teo_valmed.png', bbox_inches="tight")





