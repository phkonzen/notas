from sympy import *
var('x',real=True)

f = lambda x: (x+1)*(x-1)*(x-2)/((x-1)*(x-2))
p = plot(f(x),(x,-2,3),show=False)
p.ylabel = '$y$'
p.save('fig_ex_lim0.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.plot([1],[2],marker='o',markerfacecolor='white')
ax.plot([2],[3],marker='o',markeredgecolor='blue', markerfacecolor='white')
ax.plot([1,1],[0,2],ls='--',color='gray')
ax.plot([0,1],[2,2],ls='--',color='gray')
ax.plot([2,2],[0,3],ls='--',color='gray')
ax.plot([0,2],[3,3],ls='--',color='gray')
fig.savefig('fig_ex_lim0.png', bbox_inches='tight')
