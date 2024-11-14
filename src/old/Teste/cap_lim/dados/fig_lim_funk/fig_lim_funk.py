import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x',real=True)

p1 = plot(-1,(x,-2,2),line_color='none',show=False)
p2 = plot(1,(x,-2,2),show=False)
p3 = plot(2,(x,-2,2),line_color='none',show=False)
p = p1
p.extend(p2)
p.extend(p3)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_lim_funk.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_ylim((-1,2))
ax.set_xticks([1])
ax.set_xticklabels(['$\\rightarrow x_0 \\leftarrow$'])
ax.set_yticks([1])
ax.set_yticklabels([])
ax.text(-0.15,1.1,"$k$")
ax.plot([1,1],[0,1],ls='--',color='gray')
ax.plot([1],[1],marker='o')
fig.savefig('fig_lim_funk.png', bbox_inches='tight', transparent=True)
