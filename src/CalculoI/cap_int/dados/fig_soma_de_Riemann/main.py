#!/bin/python3
import matplotlib.pyplot as plt
from sympy import *
import numpy as np
from sympy import plot_implicit
import matplotlib.patches as patches

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 14
     })

var('x,y',real=True)

f = (x-0.5)**3 - 4*(x-0.5)**2 + 3*(x-0.5)+1 + 2.5

# pts criticos
pc = solve(f.diff())

p = plot(f,(x,0.5,3.25),line_color='blue',show=False)
q = plot(-0.5,(x,-0.5,3.75),line_color='none',show=False)
p.extend(q)
q = plot(5,(x,-0.5,3.75),line_color='none',show=False)
p.extend(q)
q = plot_implicit(y <= f, (x,0.5,3.25), (y,0,5), show=False,
                  line_color="gray")
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_soma_de_Riemann.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid('on')
ax.set_xticks([0.5,1,1.5,2,2.75,3.25])
ax.set_xticklabels(["$a=x_0$","$x_1$","$x_2$","$x_3$","$x_{n-1}$","$x_n=b$"])
ax.set_yticks([float(f.subs(x,0.5)),float(f.subs(x,3.25))])
ax.set_yticklabels([])

xs = 0.75
rect = patches.Rectangle((0.5,0),0.5,float(f.subs(x,xs)),facecolor="blue",alpha=0.5)
ax.add_patch(rect)
ax.plot([xs,xs],[-0.5,float(f.subs(x,xs))],ls='--',color="black",lw=0.75)
ax.text(xs-0.1,-0.75,"$x_1^*$")

xs = 1.3
rect = patches.Rectangle((1,0),0.5,float(f.subs(x,xs)),facecolor="blue",alpha=0.5)
ax.add_patch(rect)
ax.plot([xs,xs],[-0.5,float(f.subs(x,xs))],ls='--',color="black",lw=0.75)
ax.text(xs-0.1,-0.75,"$x_2^*$")

xs = 1.65
rect = patches.Rectangle((1.5,0),0.5,float(f.subs(x,xs)),facecolor="blue",alpha=0.5)
ax.add_patch(rect)
ax.plot([xs,xs],[-0.5,float(f.subs(x,xs))],ls='--',color="black",lw=0.75)
ax.text(xs-0.1,-0.75,"$x_3^*$")

ax.text(2.25,1,"$\\cdots$")
ax.text(2.25,-0.5,"$\\cdots$")

xs = 3
rect = patches.Rectangle((2.75,0),0.5,float(f.subs(x,xs)),facecolor="blue",alpha=0.5)
ax.add_patch(rect)
ax.plot([xs,xs],[-0.5,float(f.subs(x,xs))],ls='--',color="black",lw=0.75)
ax.text(xs-0.1,-0.75,"$x_n^*$")

ax.text(3.25,2.5,"$y=f(x)$")

fig.savefig('fig_soma_de_Riemann.png', bbox_inches="tight", transparent=True)






