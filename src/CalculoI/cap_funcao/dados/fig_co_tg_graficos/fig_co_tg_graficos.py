#!/bin/python3

import numpy as np
from sympy import *
init_printing()
var('x',real=True)

# seno
p = plot(tan(x),(x,-3*pi/2,3*pi/2),ylim=[-2,2],show=False)
p.xlabel = '$x$'
p.ylabel = '$\\mathrm{tg}(x)$'
p.save('fig_tg_grafico.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([-3*np.pi/2,-np.pi,-np.pi/2,0,np.pi/2,np.pi,3*np.pi/2])
ax.set_xticklabels(['$-\\frac{3\\pi}{2}$','$-\\pi$','$-\\frac{\\pi}{2}$','$0$','$\\frac{\\pi}{2}$',
                    '$\\pi$','$\\frac{3\\pi}{2}$'])
ax.set_yticks([-1,1])
fig.savefig('fig_tg_grafico.png')

# cosseno
p = plot(cot(x),(x,-pi,2*pi),ylim=(-2,2),show=False)
p.xlabel = '$x$'
p.ylabel = '$\\mathrm{cotg}(x)$'
p.save('fig_cotg_grafico.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi,3*np.pi/2,2*np.pi])
ax.set_xticklabels(['$-\\pi$','$-\\frac{\\pi}{2}$','$0$','$\\frac{\\pi}{2}$',
                    '$\\pi$','$\\frac{3\\pi}{2}$','$2\\pi$'])
ax.set_yticks([-1,1])
fig.savefig('fig_cotg_grafico.png')


