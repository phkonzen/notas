from sympy import *
import numpy as np
var('x',real=True)

p1 = plot((x**2-1)/(5*x-4),(x,-5,4/5-0.001),line_color='blue',show=False)
p2 = plot((x**2-1)/(5*x-4),(x,4/5+0.001,5),line_color='blue',show=False)
p = p1
p.extend(p2)
p.ylabel = '$y$'
p.save('fig_ex_ass_obl.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_ylim((-2,2))
ax.plot([4/5,4/5],[-2,2],ls='--',color='gray')
xx = np.linspace(-5,5)
ax.plot(xx,1/5*xx+4/25,ls='--',color='gray')
ax.text(2.4,1,'$y = \\frac{x}{5}+\\frac{4}{25}$')
fig.savefig('fig_ex_ass_obl.png', bbox_inches='tight')
