import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

p = plot(log(x),(x,0.001,4),line_color='blue',show=False)
q = plot(exp(x),(x,-4,4),line_color="0.5",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_aspect("equal")
ax.set_ylim((-4,4))
ax.set_xticks([-4,-3,-2,-1,0,1,2,3,4])
ax.set_xticklabels(["","","","","0","1","","",""])
ax.set_yticks([-4,-3,-2,-1,0,1,2,3,4])
ax.set_yticklabels(["","","","","","1","","",""])

ax.plot([-4,4],[-4,4],ls="--",color="0.75",lw=2)
ax.plot([0,0],[-4,5],ls="--",color="red",lw=2)
ax.text(1.5,-2,"$y = \\ln x$",
        bbox = dict(fc = "white", ec = "white"))
ax.text(-3,1,"$y = e^x$",
        bbox = dict(fc = "white", ec = "white"))
fig.savefig('fig.png', bbox_inches='tight')
