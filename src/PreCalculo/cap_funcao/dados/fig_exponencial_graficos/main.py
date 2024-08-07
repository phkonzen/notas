import numpy as np
import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x')

# 2^x
a = 2
p = plot(a**x, (x,-5,3), ylim=[0,4], show=False)
q = plot(-1, (x,-2,2), color='none', show=False)
p.extend(q)
p.xlabel = ''
p.ylabel = ''
p.title = '$f(x) = a^x, a>1$'
p.save('fig1.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([-1,0,1])
ax.set_xticklabels(['$-1$','$0$','$1$'])
ax.set_yticks([1/a,1,a])
ax.set_yticklabels(['$1/a$','$1$','$a$'])
ax.plot([-1,-1],[0,1/a],color='gray',ls='--')
ax.plot([-1,0],[1/a,1/a],color='gray',ls='--')
ax.plot([-1],[1/a],markersize=4,marker='o',color='red')
ax.plot([0],[1],markersize=4,marker='o',color='red')
ax.plot([1,1],[0,a],color='gray',ls='--')
ax.plot([0,1],[a,a],color='gray',ls='--')
ax.plot([1],[a],markersize=4,marker='o',color='red')
ax.text(-0.3,3.75,'$x$')
ax.text(2.9,-0.25,'$y$')
fig.savefig('fig1.png')

# (1/2)^x
a = 1/2
p = plot(a**x,(x,-3,5),ylim=[0,4],show=False)
q = plot(-1, (x,-2,2), color='none', show=False)
p.extend(q)
p.xlabel = ''
p.ylabel = ''
p.title = '$g(x) = a^x, 0<a<1$'
p.save('fig2.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([-1,0,1])
ax.set_xticklabels(['$-1$','$0$','$1$'])
ax.set_yticks([1/a,1,a])
ax.set_yticklabels(['$1/a$','$1$','$a$'])
ax.plot([-1,-1],[0,1/a],color='gray',ls='--')
ax.plot([-1,0],[1/a,1/a],color='gray',ls='--')
ax.plot([-1],[1/a],markersize=4,marker='o',color='red')
ax.plot([0],[1],markersize=4,marker='o',color='red')
ax.plot([1],[a],markersize=4,marker='o',color='red')
ax.plot([1,1],[0,a],color='gray',ls='--')
ax.plot([0,1],[a,a],color='gray',ls='--')
ax.text(-0.3,3.75,'$x$')
ax.text(3.9,-0.25,'$y$')
fig.savefig('fig2.png')

