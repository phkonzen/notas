import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })

var('x')

# f_1 -> f_2
p = plot(log(x),(x,-3,4),ylim=[-4,3],line_color="gray",show=False)
q = plot(log(x+2),(x,-3,4),ylim=[-4,3],line_color="gray",show=False)
p.extend(q)
q = plot(log(x+2)+1,(x,-3,4),ylim=[-4,3],line_color="blue",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_exeresol_lograf.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.text(3,1,"$y=\\ln x$")
ax.text(1,1,"$y=\\ln(x+2)$")
ax.text(2,2,"$y=\\ln(x+2)+1$")
fig.savefig('fig_exeresol_lograf.png', bbox_inches='tight')
