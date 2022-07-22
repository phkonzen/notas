import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

p = plot(-1/abs(x),(x,-5,-0.001),line_color='blue',show=False)
q = plot(-1/abs(x),(x,0.001,5),line_color='blue',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_ylim((-5,1))
ax.plot([0,0],[-5,5],ls="--",color="red",lw=2)
ax.text(0.2,0.5,"$x=0$")
ax.text(1.5, -2.5, "$\\displaystyle y = -\\frac{1}{|x|}$",
        bbox = dict(facecolor="white", edgecolor = "white"))
fig.savefig('fig.png', bbox_inches='tight')
