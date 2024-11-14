import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x', real=True)

p = plot(exp(-x),(x,-2,5),line_color='blue',show=False)
q = plot(-1,(x,-2,5),line_color='none',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_exeresol_lim_exp_xinf.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.plot([-2,5],[0,0],ls='--',lw=2,color='red')
ax.text(4,0.5,"$y = e^x$")
ax.text(-1.9,0.4,"$y = 0$",color="red")
fig.savefig('fig_exeresol_lim_exp_xinf.png', bbox_inches='tight')
