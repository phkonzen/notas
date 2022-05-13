import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })

var('x')

alpha = 2
f = lambda x: x**2

p = plot(f(x),(x,-4,4),ylim=[0,9],line_color="gray",show=False)
q = plot(alpha*f(x),(x,-4,4),ylim=[0,9],line_color="blue",show=False)
p.extend(q)
p.title = (f"$\\alpha = {alpha}$")
p.xlabel = '$x$'
p.ylabel = '$y$'
p[0].label = "$f(x) = x^2$"
p[1].label = "$\\alpha\\cdot f(x)$"
p.save('fig_ex_dilavert.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.legend(loc="upper right")
fig.savefig('fig_ex_dilavert.png', bbox_inches='tight')
