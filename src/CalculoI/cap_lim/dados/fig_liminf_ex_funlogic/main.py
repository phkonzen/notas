import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,t', real=True)

P0 = 1
K = 5
r = 1.5

P = K/(1+(K-P0)/P0*exp(-r*t))

p = plot(P, (t,0,5), line_color="blue", show=False)
q = plot(-1,(t,0,5),line_color="none",show=False)
p.extend(q)
q = plot(K+1,(t,0,5),line_color="none",show=False)
p.extend(q)
p.xlabel = '$t$'
p.ylabel = '$P$'
p.save('fig_liminf_ex_funlogic.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_yticks([P0,K])
ax.set_yticklabels(["$P_0$","$K$"])
ax.set_xticks([0])
#ax.grid()
ax.plot([0,5],[K,K],ls="--",color="red")
ax.plot([0],[P0],marker="o",markersize=4,color="blue")
fig.savefig('fig_liminf_ex_funlogic.png', bbox_inches='tight')
