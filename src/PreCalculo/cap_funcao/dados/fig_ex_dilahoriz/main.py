import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })

x = Symbol('x')

alpha = 0.5
f = Lambda(x, x**3)

p = plot(f(x),(x,-4,4),ylim=[-9,9],line_color="gray",show=False)
q = plot(f(alpha*x),(x,-4,4),ylim=[-9,9],line_color="blue",show=False)
p.extend(q)
p.title = f"$\\alpha = {alpha}$"
p.xlabel = '$x$'
p.ylabel = '$y$'
p[0].label = "$f(x) = x^3$"
p[1].label = "$f(\\alpha\\cdot x)$"
p.save('fig_ex_dilahoriz.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_yticks(range(-9,9))
ax.legend(loc="upper right")
fig.savefig('fig_ex_dilahoriz.png', bbox_inches='tight')
