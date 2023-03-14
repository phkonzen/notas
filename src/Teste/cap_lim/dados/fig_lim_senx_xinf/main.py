import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x', real=True)

p = plot(sin(x),(x,-10*pi,10*pi),line_color='blue',show=False)
q = plot(1.5,(x,-10*pi,10*pi),line_color='none',show=False)
p.extend(q)
q = plot(-1.5,(x,-20,20),line_color='none',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_lim_senx_xinf.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_xticks([])
fig.savefig('fig_lim_senx_xinf.png', bbox_inches='tight')
