import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 9,
     "font.sans-serif": "Computer Modern Roman",
     "text.latex.preamble": r"\usepackage{amsmath} \usepackage{amssymb}",
     "figure.figsize": [2.5, 2.5],
     "figure.dpi": 300
     })

fig = plt.figure()
ax = fig.add_subplot()
ax.grid()
xx = np.linspace(-1.5, 2.5, 100)
y1 = xx**2
y2 = xx + 2
ax.plot([-1.5, 2.5], [0., 0.], color='k')
ax.text(2.4, -0.25, '$x$')
ax.plot([0., 0.], [-0.3, 6.3], color='k')
ax.text(-0.15, 6.1, '$y$')
ax.plot(xx, y1, label='$y=x^2$')
ax.plot(xx, y2, label='$y=x+2$')
ax.fill_between(xx, y1, y2, where=(y1<y2), 
                alpha=0.5, color='gray')
ax.legend(loc='upper right', fontsize=9)
plt.show()
fig.savefig('fig.png', dpi=300, bbox_inches='tight')


# x,y = sym.var('x,y')
# f = x**2
# g = x + 2
# p = sym.plot(f, (x,-1.5,2.5), label='$y=f(x)$', show=False)
# q = sym.plot(g, (x,-1.5,2.5), label='$y=g(x)$', show=False)
# p.extend(q)
# q = sym.plot_implicit(sym.And(y>f, y<x+2), (x,-1,2), (y,0,4), show=False)
# p.extend(q)
# p.xlabel = '$x$'
# p.ylabel = '$y$'
# p.legend = True
# p.show()

# fig = p._backend.fig
# fig.savefig('fig.png', dpi=300, bbox_inches='tight')
