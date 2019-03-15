from sympy import *
init_printing()
var('x')

# 2^x
a = 2
p = plot(a**x,(x,-2,2),ylim=[0,4],show=False)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.title = '$f(x) = a^x, a>1$'
p.save('fig_exponencial_2.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([-1,0,1])
ax.set_xticklabels(['$-1$','$0$','$1$'])
ax.set_yticks([1/a,1,a])
ax.set_yticklabels(['$1/a$','$1$','$a$'])
ax.plot([-1,-1],[0,1/a],color='gray',ls='--')
ax.plot([-1,0],[1/a,1/a],color='gray',ls='--')
ax.plot([0],[1],markersize=4,marker='o')
ax.plot([1,1],[0,a],color='gray',ls='--')
ax.plot([0,1],[a,a],color='gray',ls='--')
fig.savefig('fig_exponencial_2.png')

# (1/2)^x
a = 1/2
p = plot(a**x,(x,-2,2),ylim=[0,4],show=False)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.title = '$g(x) = a^x, 0<a<1$'
p.save('fig_exponencial_12.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([-1,0,1])
ax.set_xticklabels(['$-1$','$0$','$1$'])
ax.set_yticks([1/a,1,a])
ax.set_yticklabels(['$1/a$','$1$','$a$'])
ax.plot([-1,-1],[0,1/a],color='gray',ls='--')
ax.plot([-1,0],[1/a,1/a],color='gray',ls='--')
ax.plot([0],[1],markersize=4,marker='o')
ax.plot([1,1],[0,a],color='gray',ls='--')
ax.plot([0,1],[a,a],color='gray',ls='--')
fig.savefig('fig_exponencial_12.png')

