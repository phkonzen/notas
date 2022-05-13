import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })

var('x')

k = 1
f = lambda x: x**2

p = plot(f(x),(x,-3,3),line_color="gray",show=False)
q = plot(f(x+k),(x,-3,3),line_color="blue",show=False)
p.extend(q)
p.title = (f"$k = {k}$")
p.xlabel = '$x$'
p.ylabel = '$y$'
p[0].label = "$f(x) = x^2$"
p[1].label = "$f(x+k)$"
p.save('fig_ex_transhoriz.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.legend(loc="upper right")
fig.savefig('fig_ex_transhoriz.png', bbox_inches='tight')
