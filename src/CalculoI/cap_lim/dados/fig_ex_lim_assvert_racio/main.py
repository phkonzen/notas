import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

f = lambda x: (x-2)*(x+2)**2/((x-1)*(x+1))

p = plot(f(x),(x,-5,-1-0.001),line_color='blue',show=False)
q = plot(f(x),(x,-1+0.001,1-0.001),line_color='blue',show=False)
p.extend(q)
q = plot(f(x),(x,1+0.001,5),line_color='blue',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_ylim((-30,30))
ax.plot([-1,-1],[-30,30],ls="--",color="red",lw=2)
ax.plot([1,1],[-30,30],ls="--",color="red",lw=2)
fig.savefig('fig.png', bbox_inches='tight')
