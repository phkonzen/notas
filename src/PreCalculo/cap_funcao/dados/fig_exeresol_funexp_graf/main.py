import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x')

# f_1 -> f_2
p = plot(exp(-x),(x,-2,5),line_color="gray",show=False)
q = plot(exp(-(x-1/2)),(x,-1,5),line_color="blue",show=False)
p.extend(q)
q = plot(-1,(x,-2,2),line_color='none',show=False,label='__none__')
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p[0].label = "$f_1(x) = e^{-x}$"
p[1].label = "$f_2(x) = e^{-(x-\\frac{1}{2})}$"
p.save('fig1.png')

fig = p._backend.fig
ax = fig.axes[0]
# ax.set_yticks(range(-8,9))
ax.grid()
ax.set_xticks([-1,-1/2,0,1/2,1,1.5])
ax.set_xticklabels(['$-1$','$-\\frac{1}{2}$','$0$','$\\frac{1}{2}$','$1$','$\\frac{3}{2}$'])
ax.set_yticks([1/E,1,E])
ax.set_yticklabels(['$e^{-1}$','$1$','$e$'])
ax.plot([-1,0,1],[E,1,1/E],ls='',marker='o',color='gray')
ax.plot([-0.5,0.5,1.5],[E,1,1/E],ls='',marker='o',color='blue')
ax.legend(loc="upper right")
fig.savefig('fig1.png', bbox_inches='tight')

# f_2 -> f_3
p = plot(exp(-(x-1/2)),(x,-1.55,5),line_color="gray",show=False)
q = plot(exp(-2*(x-1/2)),(x,-0.55,5),line_color="blue",show=False)
p.extend(q)
q = plot(-1,(x,-2,2),line_color='none',show=False,label='__none__')
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p[0].label = "$f_1(x) = e^{-(x-\\frac{1}{2})}$"
p[1].label = "$f_2(x) = e^{-2(x-\\frac{1}{2})}$"
p.save('fig2.png')

fig = p._backend.fig
ax = fig.axes[0]
# ax.set_yticks(range(-8,9))
ax.grid()
ax.legend(loc="upper right")
ax.set_xticks([-3/2,-1/2,1/2,1.5])
ax.set_xticklabels(['$-\\frac{3}{2}$','$-\\frac{1}{2}$','$\\frac{1}{2}$','$\\frac{3}{2}$'])
ax.set_yticks([1/E,1/E**2,1,E,E**2])
ax.set_yticklabels(['$e^{-1}$','$e^{-2}$','$1$','$e$','$e^2$'])
ax.plot([-1.5,-0.5,0.5,1.5],[E**2,E,1,1/E],ls='',marker='o',color='gray')
ax.plot([-0.5,0.5,1.5],[E**2,1,1/E**2],ls='',marker='o',color='blue')
fig.savefig('fig2.png', bbox_inches='tight')

# f_3 -> f_4
p = plot(exp(-2*(x-1/2)),(x,-0.55,5),line_color="gray",show=False)
q = plot(exp(-2*(x-1/2))-1,(x,-0.55,5),line_color="blue",show=False)
p.extend(q)
q = plot(-2.5,(x,-2,2),line_color='none',show=False,label='__none__')
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p[0].label = "$f_1(x) = e^{-2(x-\\frac{1}{2})}$"
p[1].label = "$f_2(x) = e^{-2(x-\\frac{1}{2})}-1$"
p.save('fig3.png')

fig = p._backend.fig
ax = fig.axes[0]
# ax.set_yticks(range(-8,9))
ax.grid()
ax.legend(loc="upper right")
ax.set_xticks([-1/2,1/2,3/2])
ax.set_xticklabels(['$-\\frac{1}{2}$','$\\frac{1}{2}$','$\\frac{3}{2}$'])
ax.set_yticks([1/E**2,1/E**2-1,1,0,E**2,E**2-1])
ax.set_yticklabels(['$e^{-2}$','$e^{-2}-1$','$1$','$0$','$e^2$','$e^2$-1'])
ax.plot([-0.5,0.5,1.5],[E**2,1,1/E**2],ls='',marker='o',color='gray')
ax.plot([-0.5,0.5,1.5],[E**2-1,0,1/E**2-1],ls='',marker='o',color='blue')
fig.savefig('fig3.png', bbox_inches='tight')

