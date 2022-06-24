#!/bin/python3


import numpy as np
import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })


var('x',real=True)

# seno
p1 = plot(tan(x),(x,-3*pi/2,-pi/2-0.01),ylim=[-3,3],show=False)
p2 = plot(tan(x),(x,-pi/2,pi/2),ylim=[-3,3],show=False)
p3 = plot(tan(x),(x,pi/2+0.01,3*pi/2),ylim=[-3,3],show=False)
p = p1
p.extend(p2)
p.extend(p3)
p.xlabel = '$x$'
p.ylabel = '$\\mathrm{tg}(x)$'
p.save('fig_tg_grafico.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([-3*np.pi/2,-np.pi,-np.pi/2,0,np.pi/2,np.pi,3*np.pi/2])
ax.set_xticklabels(['$-\\frac{3\\pi}{2}$','$-\\pi$',
                    '$-\\frac{\\pi}{2}$','$0$','$\\frac{\\pi}{2}$',
                    '$\\pi$','$\\frac{3\\pi}{2}$'])
ax.set_yticks([-1,1])
ax.set_ylim((-3,3))
ax.grid()
ax.plot([-3*pi/2,-3*pi/2],[-2,2],ls='--',color='gray')
ax.plot([-pi/2,-pi/2],[-2,2],ls='--',color='gray')
ax.plot([pi/2,pi/2],[-2,2],ls='--',color='gray')
ax.plot([3*pi/2,3*pi/2],[-2,2],ls='--',color='gray')
ax.set_ylim((-2,2))
fig.savefig('fig_tg_grafico.png', bbox_inches="tight")

# cosseno
p1 = plot(cot(x),(x,-pi,0-0.01),ylim=(-3,3),show=False)
p2 = plot(cot(x),(x,0+0.01,pi-0.01),ylim=(-3,3),show=False)
p3 = plot(cot(x),(x,pi+0.01,2*pi-0.01),ylim=(-3,3),show=False)
p = p1
p.extend(p2)
p.extend(p3)
p.xlabel = '$x$'
p.ylabel = '$\\mathrm{cotg}(x)$'
p.save('fig_cotg_grafico.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi,3*np.pi/2,2*np.pi])
ax.set_xticklabels(['$-\\pi$','$-\\frac{\\pi}{2}$','$0$','$\\frac{\\pi}{2}$',
                    '$\\pi$','$\\frac{3\\pi}{2}$','$2\\pi$'])
ax.set_yticks([-1,1])
ax.set_ylim((-3,3))
ax.grid()
ax.plot([-pi,-pi],[-2,2],ls='--',color='gray')
ax.plot([0,0],[-2,2],ls='--',color='gray')
ax.plot([pi,pi],[-2,2],ls='--',color='gray')
ax.plot([2*pi,2*pi],[-2,2],ls='--',color='gray')
ax.set_ylim((-2,2))

fig.savefig('fig_cotg_grafico.png', bbox_inches="tight")


