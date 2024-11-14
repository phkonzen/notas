import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

p = plot(exp(x),(x,-5,2),line_color='blue',show=False)
q = plot(-1,(x,-5,2),line_color='none',show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_ex_xinf_exp.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.plot([-5,2],[0,0],ls='--',lw=2,color='red')
ax.text(1.25,0.25,"$y = 0$",color="red")
ax.text(1,6.5,"$y = e^x$")
fig.savefig('fig_ex_xinf_exp.png', bbox_inches='tight')
