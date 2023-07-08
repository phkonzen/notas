import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })

x,y = sym.var('x,y')
f = x**2
g = x + 2
p = sym.plot(f, (x,-1.5,2.5), label='$y=f(x)$', show=False)
q = sym.plot(g, (x,-1.5,2.5), label='$y=g(x)$', show=False)
p.extend(q)
q = sym.plot_implicit(sym.And(y>f, y<x+2), (x,-1,2), (y,0,4), show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.legend = True
p.save('fig.pdf')
p.save('fig.png')
