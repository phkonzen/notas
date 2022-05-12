import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })


var('x')

p=plot(0.5*x,(x,-2,2),line_color='blue',show=False)
q=plot(x,(x,-2,2),line_color='red',show=False)
p.extend(q)
q=plot(2*x,(x,-2,2),line_color='green',show=False)
p.extend(q)
q=plot(-2*x,(x,-2,2),line_color='green',show=False)
p.extend(q)
q=plot(-x,(x,-2,2),line_color='red',show=False)
p.extend(q)
q=plot(-0.5*x,(x,-2,2),line_color='blue',show=False)
p.extend(q)
p.xlabel="$x$"
p.ylabel="$y$"
p.save('fig_ex_funlinear.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.text(1.5,0.45,'$y=\\frac{1}{2}x$',color='blue')
ax.text(1.5,1.1,'$y=x$',color='red')
ax.text(1.5,2.8,'$y=2x$',color='green')
ax.text(-1.5,3.1,'$y=-2x$',color='green')
ax.text(-1.5,1.7,'$y=-x$',color='red')
ax.text(-1.5,0.7,'$y=-\\frac{1}{2}x$',color='blue')

fig.savefig('fig_ex_funlinear.png')
