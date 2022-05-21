import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 14
     })

var('x',real=True)

f=sin(x)

x0=0.5
y0=sin(x0)
x1=1.25
y1=sin(x1)

rs = (y1-y0)/(x1-x0)*(x-x0)+y0
rt = cos(x0)*(x-x0)+y0

p1 = plot(f,(x,-0.5,2),line_color='blue',show=False)
p2 = plot(rs,(x,-0.5,1.75),line_color='green',show=False)
p3 = plot(rt,(x,-0.5,1.75),line_color='red',show=False)
p = p1
p.extend(p2)
p.extend(p3)
p.ylabel = '$y$'
p.save('fig_retsectg.png')


fig = p._backend.fig
ax = fig.axes[0]
ax.set_yticks([0,y0,y1])
ax.set_yticklabels(['$0$','$f(x_0)$','$f(x_1)$'],
                   fontsize=12)
ax.set_xticks([0,x0,x1])
ax.set_xticklabels(['$0$','$x_0$','$x_1$'],
                   fontsize=12)
ax.plot([x0],[y0],marker="o",markersize=4,color="blue")
ax.plot([x1],[y1],marker="o",markersize=4,color="blue")
ax.plot([x0,x0],[0,y0],ls='--',color='gray')
ax.plot([0,x1],[y0,y0],ls='--',color='gray')
ax.plot([x0,x1],[y0,y0],ls='--',color='black')
ax.plot([x1,x1],[0,y1],ls='--',color='gray')
ax.plot([x1,x1],[y0,y1],ls='--',color='black')
ax.plot([0,x1],[y1,y1],ls='--',color='gray')
ax.text(x1+0.1,y0+0.2,'$f(x_1)-f(x_0)$',
        fontsize=12)
ax.text(x0+0.2,y0-0.075,'$x_1-x_0$',
        fontsize=12)
ax.text(x1-0.5,y1+0.2,'reta tangente',
        fontsize=12)
ax.text(x1+0.5,y1+0.2,'reta secante',
        fontsize=12)
fig.savefig('fig_retsectg.png', bbox_inches='tight', transparent=True)
