import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt

# use LaTeX
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 12,
    "savefig.bbox": 'tight'})
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_aspect('equal', 'box')
ax.set_xlim([-2.5,2.5])
ax.set_ylim([-2.5,2.5])
ax.grid()

ax.set_xticks([-2,-1,0,1,2])
ax.set_yticks([-2,-1,0,1,2])

ax.arrow(-2.5,0,5,0,
         length_includes_head=True,
         head_width=0.1,
         head_length=0.1,
         color='black')
ax.text(2.2,-0.4,"$x_1$")

ax.arrow(0,-2.5,0,5,
         length_includes_head=True,
         head_width=0.1,
         head_length=0.1,
         color='black')
ax.text(-0.3,2.2,"$x_2$")

ax.plot([1],[1],
        marker='$\\oplus$',markersize=10,
        color='blue')
ax.plot([1,-1,-1],[-1,1,-1], ls="",
        marker='$\\ominus$',markersize=10,
        color='red')

# pesos e bias
w = np.array([1.,1.])
b = -1.

xx = np.linspace(-3,3)
yy = -(w[0]*xx+b)/w[1]
ax.plot(xx, yy, color="black")

ax.text(2.1, 2.1, "$\\tau^+$", backgroundcolor="white")
ax.fill_between(xx, yy, 2.5*np.ones_like(xx),
                color="blue", alpha=0.1)
ax.text(-1.9, -1.9, "$\\tau^-$", backgroundcolor="white")
ax.fill_between(xx, -2.5*np.ones_like(xx), yy,
                color="red", alpha=0.1)

x = 1
y = -(w[0]*x+b)/w[1]
nt = np.linalg.norm(w)
ax.arrow(x,y,w[0],w[1],
         length_includes_head=True,
         head_width=0.1,
         head_length=0.1,         
         color='black')
ax.text(x+w[0]-0.6,y+w[1]+0.16,'$\\pmb{w}=(1,1)$',
        color='black', backgroundcolor="white")

nt = np.linalg.norm(w)
d = -b/nt
ax.plot([0,d*w[0]/nt],[0,d*w[1]/nt],
        marker="|", color="green")
ax.text(0.1,-0.5,"$\\displaystyle\\frac{|b|}{\|\\pmb{w}\|}$",
        color="green", backgroundcolor="white")

ax.text(-0.05,1.3,'$\\pmb{w}\\cdot\\pmb{x}+b=0$',
        color="black", backgroundcolor="white")

fig.savefig("main.png")
plt.show()
