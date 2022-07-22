import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

f = lambda x: 1/x**2

p = plot(f(x), (x,-5,-1e-5), line_color="blue", show=False)
q = plot(f(x), (x,1e-5,5), line_color="blue", show=False)
p.extend(q)
q = plot(-1, (x,-5,5), line_color="none", show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_ylim((-1,40))
ax.plot([0,0],[-1,40],ls="--",color="red",zorder=5)
ax.text(0.7,33,"$\\displaystyle y=\\frac{1}{x^2}$")
fig.savefig('fig.png', bbox_inches='tight')
