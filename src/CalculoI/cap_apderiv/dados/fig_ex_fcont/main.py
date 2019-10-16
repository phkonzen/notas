#!/bin/python3

import numpy as np
from sympy import *
init_printing()
var('x',real=True)

# a) f(x) = (x-1)^2+1
p = plot((x-1)**2+1,(x,0,1.5),show=False)
q = plot(-0.5,(x,-0.5,2),line_color='none',show=False)
p.extend(q)
q = plot(2.5,(x,-0.5,2),line_color='none',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_f.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.plot([1],[1],marker='o',color='red')
ax.plot([0],[2],marker='o',color='red')
ax.plot([1.5],[(1.5-1)**2+1],marker='o',color='blue',zorder=10)
ax.plot([1.5,1.5],[0,0.5**2+1],ls='--',color='gray')
fig.savefig('fig_f.png')

# b) g(x) = \ln x
p = plot(log(x),(x,0.01,E),ylim=[-4,2],show=False)
q = plot(2,(x,-1,3),line_color='none',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_g.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([-1,0,1,2.7182])
ax.set_xticklabels(["$-1$","$0$","$1$","$e$"])
ax.plot([E],[1],marker='o',color='red',zorder=12)
ax.plot([E,E],[0,1],ls='--',color='gray')
ax.plot([0,E],[1,1],ls='--',color='gray')
fig.savefig('fig_g.png')

# c) h(x) = x, 0<=x<1; h(x) = 0, x=1.
p = plot(x,(x,0,1),ylim=[-0.5,1.5],show=False)
q = plot(-0.5,(x,-0.5,1.5),line_color='none',show=False)
p.extend(q)
q = plot(1.5,(x,-0.5,1.5),line_color='none',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_h.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([0,1])
ax.set_xticklabels(["$0$","$1$"])
ax.set_yticks([0,1])
ax.set_yticklabels(["$0$","$1$"])
ax.plot([0],[0],marker='o',color='red')
ax.plot([1],[1],marker='o',color='blue',markerfacecolor='white',zorder=10)
ax.plot([1],[0],marker='o',color='blue')
ax.plot([1,1],[0,1],ls='--',color='gray')
ax.plot([0,1],[1,1],ls='--',color='gray')
fig.savefig('fig_h.png', bbox_inches="tight")




