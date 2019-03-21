from sympy import *
var('x',real=True)

p = plot(x,(x,-1,2),show=False)
p.ylabel = '$y$'
p.save('fig_lim_funid.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([1])
ax.set_xticklabels(['$\\rightarrow x_0 \\leftarrow$'])
ax.set_yticks([1])
ax.set_yticklabels(['$x_0$'])
ax.plot([1,1],[0,1],ls='--',color='gray')
ax.plot([0,1],[1,1],ls='--',color='gray')
ax.plot([1],[1],marker='o')
fig.savefig('fig_lim_funid.png', bbox_inches='tight')
