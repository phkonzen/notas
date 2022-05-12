import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })


var('x')

r = (x+1)*(x-2)/((x**2+1)*(x-1))
print(latex(expand(r)))
p1 = plot(r,(x,-5,1-0.01),ylim=[-5,5],show=False)
p2 = plot(r,(x,1+0.01,5),ylim=[-5,5],show=False)
p = p1
p.extend(p2)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_racional_grafico.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.plot([1,1],[-5,5],ls='--',color='gray')
ax.set_ylim((-5,5))
ax.grid()
fig.savefig('fig_racional_grafico.png', bbox_inches='tight')
