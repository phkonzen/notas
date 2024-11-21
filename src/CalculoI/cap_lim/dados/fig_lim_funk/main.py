import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12,
     "font.sans-serif": "Computer Modern Roman",
     "text.latex.preamble": r"\usepackage{amsmath} \usepackage{amssymb}",
     "figure.figsize": [4, 4],
     "figure.dpi": 300
     })

var('x',real=True)

p1 = plot(-1,(x,-2,2),line_color='none',show=False)
p2 = plot(1,(x,-2,2),show=False)
p3 = plot(2,(x,-2,2),line_color='none',show=False)
p = p1
p.extend(p2)
p.extend(p3)
p.xlabel = ''
p.ylabel = ''
p.save('fig.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_ylim((-1,2))
ax.set_xticks([1])
ax.set_xticklabels(['$\\rightarrow x_0 \\leftarrow$'])
ax.set_yticks([1])
ax.set_yticklabels([])
ax.text(2, -0.15, '$x$')
ax.text(-0.2, 1.8, '$y$')
ax.text(-0.15,1.1,"$k$")
ax.plot([1,1],[0,1],ls='--',color='gray')
ax.plot([1],[1],marker='o')
fig.savefig('fig.png', bbox_inches='tight')
