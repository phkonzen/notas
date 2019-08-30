from sympy import *
var('x,y', real=True)

f = lambda x: 5*cos(x)*exp(0.4*x)+2

M = 6

p = plot(f(-x), (x,-3,15), line_color="blue", show=False)
q = plot(-1,(x,-3,15),line_color="none",show=False)
p.extend(q)
q = plot_implicit(y<f(-x),(x,M,15),(y,0,5),
                  line_color="gray",show=False)
p.extend(q)

q = plot_implicit(And(y<10,y>f(-M)),(x,0,15),(y,0,f(-M)),
                  line_color="gray",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_lim_x2infty.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.set_yticks([])
ax.set_xticks([])
ax.grid()
ax.set_ylim((-1,8))
ax.text(M,-0.4,"$x \\rightarrow \infty$",fontsize=12)
ax.plot([-3,15],[2,2],ls='--',color="red")
ax.plot([M,M],[0,f(-M)+1],ls='--',color="green")
ax.text(-0.15,2+0.5,"$\\downarrow$")
ax.text(-0.15,2-0.5,"$\\uparrow$")
ax.text(-0.5,2+0.1,"$L$",fontsize=12)
fig.savefig('fig_lim_x2infty.png', bbox_inches='tight')
