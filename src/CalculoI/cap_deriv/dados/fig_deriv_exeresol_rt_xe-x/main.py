import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

f = x*exp(-x)
x0 = 1

p = plot(f, (x,-1,4), line_color="blue", show=False)
q = plot(exp(-1),(x,0.2,1.8),line_color="red",show=False)
p.extend(q)
q = plot(1,(x,-1,4),line_color="none",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
#ax.set_ylim((-2,6))
ax.set_yticks((-E,-1,1/E,1))
ax.set_yticklabels(["$-e$","$-1$","$e^{-1}$","$1$"])
ax.plot([x0],[exp(-1)],marker="o",markersize=4,color="red")
fig.savefig('fig.png', bbox_inches='tight')
