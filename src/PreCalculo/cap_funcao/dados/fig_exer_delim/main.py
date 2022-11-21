import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })


var('x,y')

p=plot(0, (x,-2,2),line_color='blue',show=False)
q=plot(2*x+2,(x,-2,2),line_color='blue',show=False)
p.extend(q)
q=plot_implicit(And(y>0, y<2*x+2),(x,-1,1),line_color='gray',show=False)
p.extend(q)
p.xlabel="$x$"
p.ylabel="$y$"

p.save('fig.png')
fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.plot([1,1],[-2,6],ls='-',color='blue')
fig.savefig('fig.png')
