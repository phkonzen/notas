import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })


var('x')

p=plot(-5/2,(x,-2,2),line_color='blue',show=False)
q=plot(2,(x,-2,2),line_color='red',show=False)
p.extend(q)
q=plot(2*x-1,(x,-2,2),line_color='green',show=False)
p.extend(q)
p[0].label="$y=-5/2$"
p[1].label="$y=2$"
p[2].label="$y=2x-1$"
p.legend=True
p.xlabel="$x$"
p.ylabel="$y$"
p.save('fig_ex_funafim.png')
fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
fig.savefig('fig_ex_funafim.png')
