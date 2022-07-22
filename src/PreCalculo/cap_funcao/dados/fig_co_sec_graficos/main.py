import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

th = 1e-2

# secante
p = plot(sec(x),(x,-3*pi/2+th,-pi/2-th),ylim=[-4,4],show=False)
q = plot(sec(x),(x,-pi/2+th,pi/2-th),ylim=[-4,4],show=False)
p.extend(q)
q = plot(sec(x),(x,pi/2+th,3*pi/2-th),ylim=[-4,4],show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$\\mathrm{sec}(x)$'
p.save('fig_sec_grafico.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_xticks([-3*pi/2,-pi,-pi/2,0,pi/2,pi,3*pi/2])
ax.set_xticklabels(['$-\\frac{3\\pi}{2}$','$-\\pi$',
                    '$-\\frac{\\pi}{2}$','$0$',
                    '$\\frac{\\pi}{2}$','$\\pi$','$\\frac{3\\pi}{2}$'],
                   fontsize=12)
ax.set_yticks([-1,1])
ax.set_ylim([-4,4])
ax.grid()
ax.plot([-3*pi/2,-3*pi/2],[-4,4],ls="--",color="gray",zorder=0)
ax.plot([-pi/2,-pi/2],[-4,4],ls="--",color="gray",zorder=0)
ax.plot([pi/2,pi/2],[-4,4],ls="--",color="gray",zorder=0)
ax.plot([3*pi/2,3*pi/2],[-4,4],ls="--",color="gray",zorder=0)
fig.savefig('fig_sec_grafico.png', bbox_inches="tight")

# cossecante
p = plot(csc(x),(x,-pi+th,0-th),ylim=(-4,4),show=False)
q = plot(csc(x),(x,0+th,pi-th),ylim=(-4,4),show=False)
p.extend(q)
q = plot(csc(x),(x,pi+th,2*pi-th),ylim=(-4,4),show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$\\mathrm{cossec}(x)$'
p.save('fig_cosec_grafico.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_xticks([-pi,-pi/2,0,pi/2,pi,3*pi/2,2*pi])
ax.set_xticklabels(['$-\\pi$','$-\\frac{\\pi}{2}$','$0$','$\\frac{\\pi}{2}$',
                    '$\\pi$','$\\frac{3\\pi}{2}$','$2\\pi$'])
ax.set_yticks([-1,1])
ax.set_ylim((-4,4))
ax.plot([-pi,-pi],[-4,4],ls="--",color="gray",zorder=0)
ax.plot([0,0],[-4,4],ls="--",color="gray",zorder=0)
ax.plot([pi,pi],[-4,4],ls="--",color="gray",zorder=0)
ax.plot([2*pi,2*pi],[-4,4],ls="--",color="gray",zorder=0)
fig.savefig('fig_cosec_grafico.png', bbox_inches="tight")


