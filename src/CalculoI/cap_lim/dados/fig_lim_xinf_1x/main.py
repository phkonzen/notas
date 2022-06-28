import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

p = plot(1/x, (x,-5,-0.001), line_color="blue", show=False)
q = plot(1/x, (x,0.001,5), line_color="blue", show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_lim_xinf_1x.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_ylim((-5,5))
fig.savefig('fig_lim_xinf_1x.png', bbox_inches='tight')
