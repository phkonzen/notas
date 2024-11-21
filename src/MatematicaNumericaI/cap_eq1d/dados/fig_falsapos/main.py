import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12,
     "font.sans-serif": "Computer Modern Roman",
     "text.latex.preamble": r"\usepackage{amsmath} \usepackage{amssymb}"
     })

f = lambda x: np.cos(x)

fig = plt.figure(figsize=[4,4], dpi=300)
ax = fig.add_subplot()

ax.set_xlim((-np.pi/6, np.pi))
xx = np.linspace(-np.pi/6, np.pi)
ax.plot([-np.pi/6, np.pi], [0, 0], color='black')

ax.plot(xx, f(xx))

a = 0.25
ax.plot(a, f(a), marker='o', color='blue', label='função')

b = 2.
ax.plot(b, f(b), marker='o', color='blue')

rs = lambda x: (f(b)-f(a))/(b-a)*(x-a) + f(a)

xx = np.linspace(0., 2.25)
ax.plot(xx, rs(xx), color='green', label='reta secante')

xa = a - (b-a)/(f(b)-f(a))*f(a)
ax.plot(xa, rs(xa), marker='o', color="green")

xs = np.pi/2
ax.plot(xs, f(xs), marker='o', color="red")

ax.set_xticks([a, xs, b],
              ['$a$', '$x^*$', 'b'])
ax.set_yticks([f(a), 0, f(b)],
              ['$f(a)$', '$0$', '$f(b)$'])

ax.legend()
ax.grid()

fig.savefig('fig.png', bbox_inches='tight')
