import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })


var('x',real=True)

p = plot(sqrt(x),(x,-0.5,2),ylim=(-2,2),show=False,
         line_color="blue")
q = plot(x**(3/2),(x,-0.5,2),ylim=(-2,2),show=False,
         line_color="red")
p.extend(q)
p[0].label="$y=\sqrt{x}$"
p[1].label="$y=\sqrt{x^3}$"
p.legend = True
p.ylabel="$y$"
p.save('fig_funpot_racional_par.png')
fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.legend(loc='center right')
fig.savefig('fig_funpot_racional_par.png',bbox_inches='tight')

p = plot(real_root(x,3),(x,-2,2),ylim=(-2,2),show=False,
          line_color="blue")
q = plot(real_root(x**2,3),(x,-2,2),ylim=(-2,2),show=False,
         line_color="red")
p.extend(q)
p[0].label="$y=\sqrt[3]{x}$"
p[1].label="$y=\sqrt[3]{x^2}$"
p.legend = True
p.ylabel="$y$"
p.save('fig_funpot_racional_impar.png')
fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.legend(loc='center right')
fig.savefig('fig_funpot_racional_impar.png',bbox_inches='tight')
