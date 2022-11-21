import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })


var('x,y')

p=plot(x+1, (x,-1,3),line_color='blue',show=False)
q=plot(-3*x+5,(x,-1,3),line_color='blue',show=False)
p.extend(q)
q=plot_implicit(And(y>x+1, y<-3*x+5),(x,0,1),line_color='gray',show=False)
p.extend(q)
q=plot_implicit(And(y<x+1, y>-3*x+5),(x,1,2),line_color='gray',show=False)
p.extend(q)
p.xlabel="$x$"
p.ylabel="$y$"

p.save('fig.png')
fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.plot([0,0],[-5,9],ls='-',color='blue')
ax.plot([2,2],[-5,9],ls='-',color='blue')
ax.text(0.1,0.5,"$y=x+1$")
ax.text(0.5,3.75,"$y=-3x+5$")
ax.text(0.05,8,"$x=0$")
ax.text(2.05,8,"$x=2$")
fig.savefig('fig.png')
