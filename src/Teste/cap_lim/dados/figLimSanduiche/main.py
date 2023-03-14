import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

p = plot(sin(1./(x-1)**2)*(x-1)**2+1, (x,-0.1,1), ylim=[-0.1,2],
         line_color="red", show=False)
q = plot(-sin(1/(x-1)**2)*(x-1)**2+1, (x,1,2.1), ylim=[-0.1,2],
         line_color="red", show=False)
p.extend(q)
q = plot((x-1)**2+1, (x,-0.1,2.1), ylim=[-1,1],
         line_color="blue", show=False)
p.extend(q)
q = plot(-(x-1)**2+1, (x,-0.1,2.1), ylim=[-1,1],
         line_color="blue", show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_yticks([])
ax.set_xticks([])
ax.grid()

ax.text(1.3,1.5,"$y=h(x)$",color="blue")
ax.text(1.6,1,"$y=f(x)$",color="red")
ax.text(1.3,0.475,"$y=g(x)$",color="blue")

ax.text(1,-0.1,"$a$")
ax.plot([1,1],[0,1],ls="--",color="gray")
ax.plot([0,1],[1,1],ls="--",color="gray")
ax.text(-0.1,1,"$L$")
fig.savefig('fig.png', bbox_inches='tight')
