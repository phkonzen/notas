import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 16
})


var('x')

# log_2 x
a = 2
p = plot(log(x,a),(x,-0.5,4),show=False)
q = plot(a**x,(x,-4,4),line_color='gray',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig1.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_ylim((-4,4))
ax.set_xticks([0,1,a])
ax.set_xticklabels(['$0$','$1$','$a$'])
ax.set_yticks([-1,0,1])
ax.set_yticklabels(['$-1$','$0$','$1$'])
ax.plot([1],[0],markersize=4,marker='o')
ax.plot([0,a],[1,1],color='gray',ls='--')
ax.plot([a,a],[0,1],color='gray',ls='--')
ax.plot([-4,4],[-4,4],color='gray',ls='--')
ax.text(-a,0.5,'$y = a^{x}$',color='gray')
ax.text(2.5,1,'$y=log_a x, a>1$',color='blue')
fig.savefig('fig1.png')

# (1/2)^x
a = 1/2
p = plot(log(x,a),(x,-2,4),show=False)
q = plot(a**x,(x,-2,4),line_color='gray',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig2.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_ylim((-2,4))
ax.set_xticks([-1,0,a,1])
ax.set_xticklabels(['$-1$','$0$','$a$','$1$'])
ax.set_yticks([-1,0,1])
ax.set_yticklabels(['$-1$','$0$','$1$'])
ax.plot([1],[0],markersize=4,marker='o')
ax.text(0.25,3,'$y=\\log_a x, 0<a<1$',color='blue')
ax.text(3,0.25,'$y=a^x$',color='gray')
ax.plot([-2,4],[-2,4],color='gray',ls='--')
ax.plot([0,a],[1,1],color='gray',ls='--')
ax.plot([a,a],[0,1],color='gray',ls='--')
fig.savefig('fig2.png')

