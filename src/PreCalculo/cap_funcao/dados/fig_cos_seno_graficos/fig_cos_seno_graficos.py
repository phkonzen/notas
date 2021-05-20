#!/bin/python3

import numpy as np
from sympy import *
init_printing()
var('x',real=True)

# seno
p = plot(sin(x),(x,-pi,2*pi),show=False)
p.xlabel = '$x$'
p.ylabel = '$\\mathrm{sen}(x)$'
p.save('fig_seno_grafico.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi,3*np.pi/2,2*np.pi])
ax.set_xticklabels(['$-\\pi$','$-\\frac{\\pi}{2}$','$0$','$\\frac{\\pi}{2}$',
                    '$\\pi$','$\\frac{3\\pi}{2}$','$2\\pi$'])
ax.set_yticks([-1,1])
fig.savefig('fig_seno_grafico.png')

# cosseno
p = plot(cos(x),(x,-pi,2*pi),show=False)
p.xlabel = '$x$'
p.ylabel = '$\\mathrm{cos}(x)$'
p.save('fig_cosseno_grafico.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi,3*np.pi/2,2*np.pi])
ax.set_xticklabels(['$-\\pi$','$-\\frac{\\pi}{2}$','$0$','$\\frac{\\pi}{2}$',
                    '$\\pi$','$\\frac{3\\pi}{2}$','$2\\pi$'])
ax.set_yticks([-1,1])
fig.savefig('fig_cosseno_grafico.png')


