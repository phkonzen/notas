from sympy import *
var('x',real=True)

p1 = plot((x-2)/((x-2)*(x+1)),(x,-3,-1-0.0001),line_color='blue',show=False)
p2 = plot((x-2)/((x-2)*(x+1)),(x,-1+0.0001,3),line_color='blue',show=False)
p = p1
p.extend(p2)
p.ylabel = '$y$'
p.save('fig_ex_conta.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_ylim((-10,5))
ax.plot([2,2],[1/3,1/3],marker='o',markeredgecolor='blue',markerfacecolor='white')
ax.plot([2,2],[-4,-4],marker='o',markeredgecolor='blue',markerfacecolor='blue')
ax.plot([-1,-1],[-10,5],ls='--',color='gray')
ax.plot([0,2],[-4,-4],ls='--',color='gray')
ax.plot([2,2],[-4,0],ls='--',color='gray')
fig.savefig('fig_ex_conta.png', bbox_inches='tight')
