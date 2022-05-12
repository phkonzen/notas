import matplotlib.pyplot as plt
from sympy import *
from sympy.abc import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })

p = plot(x**2,(x,-2,2),ylim=(-0.5,2),show=False,
         line_color="blue")
q = plot(x**4,(x,-2,2),ylim=(-0.5,2),show=False,
         line_color="red")
p.extend(q)
q = plot(x**6,(x,-2,2),ylim=(-0.5,2),show=False,
         line_color="green")
p.extend(q)
p[0].label="$y=x^2$"
p[1].label="$y=x^4$"
p[2].label="$y=x^6$"
p.legend = True
p.ylabel="$y$"
p.save('fig_funpot_par.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.legend(loc='center right')
fig.savefig('fig_funpot_par.png',bbox_inches='tight')
