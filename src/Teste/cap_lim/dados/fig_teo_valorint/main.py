import matplotlib as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

var('x,y', real=True)

def f(x):
    return x**2

p = plot(f(x), (x,0.1,2), line_color="blue", show=False)
q = plot(-0.2, (x,-0.2,2),line_color="none",show=False)
p.extend(q)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_cap_funcao_funabs.png')

fig = p._backend.fig
ax = fig.axes[0]
ax.grid()
ax.set_xticks([])
ax.set_yticks([])

a = 0.75
ax.text(-0.2, f(a), "$f(a)$")
ax.text(a, -0.2, "$a$")
ax.plot([a,a],[0,f(a)],ls="--",color="gray")
ax.plot([a],[f(a)],marker="o",markersize=6,color="blue")
ax.plot([0,a],[f(a),f(a)],ls="--",color="gray")

b = 1.75
ax.text(-0.2, f(b), "$f(b)$")
ax.text(b, -0.2, "$b$")
ax.plot([b,b],[0,f(b)],ls="--",color="gray")
ax.plot([b],[f(b)],marker="o",markersize=6,color="blue")
ax.plot([0,b],[f(b),f(b)],ls="--",color="gray")

d = 2
c = solve(Eq(f(x),d),x)[1]
ax.text(-0.2, d, "$d$")
ax.text(c, -0.2, "$c$")
ax.plot([c,c],[0,d],ls="--",color="red")
ax.plot([c],[d],marker="o",markersize=6,color="red")
ax.plot([0,c],[d,d],ls="--",color="red")


fig.savefig('fig.png', bbox_inches='tight')
