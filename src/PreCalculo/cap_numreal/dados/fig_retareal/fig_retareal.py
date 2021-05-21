import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 12,
    'text.latex.preamble': r'\usepackage{amsfonts}'
})

fig, ax = plt.subplots()
fig.set_size_inches(6.4,1.05)
ax.axis("off")
ax.set_xlim((-4,4))
ax.set_ylim((-0.2,0.1))
ax.arrow(0,0,4,0,
         length_includes_head=True,
         head_width = 0.025,
         head_length = 0.1,
         overhang=1.0)
ax.arrow(0,0,-4,0,
         length_includes_head=True,
         head_width = 0.025,
         head_length = 0.1,
         overhang=1.0)
ax.plot([0,0],[-0.03,0.03],color="black")
ax.text(0, -0.1, "0")
ax.plot([1/2,1/2],[-0.01,0.01],color="black")
ax.text(1/2, -0.1, r'$\frac{1}{2}$')
ax.plot([1,1],[-0.02,0.02],color="black")
ax.text(1, -0.1, "1")
ax.plot([4/3,4/3],[-0.01,0.01],color="black")
ax.plot([5/3,5/3],[-0.01,0.01],color="black")
ax.text(5/3, -0.1, r'$\frac{5}{3}$')
ax.plot([2,2],[-0.02,0.02],color="black")
ax.text(2, -0.1, "2")
ax.plot([3,3],[-0.02,0.02],color="black")
ax.text(3, -0.1, "3")
ax.text(3.7, -0.1, r'$\mathbb{R}$')

ax.plot([-1,-1],[-0.02,0.02],color="black")
ax.text(-1-0.1, -0.1, "-1")
ax.plot([-3/2,-3/2],[-0.01,0.01],color="black")
ax.text(-3/2-0.15, -0.1, r'$-\frac{3}{2}$')
ax.plot([-2,-2],[-0.02,0.02],color="black")
ax.text(-2-0.1, -0.1, "-2")
ax.plot([-3,-3],[-0.02,0.02],color="black")
ax.text(-3-0.1, -0.1, "-3")

plt.savefig("fig_retareal.png", bbox_inches='tight', pad_inches=0)
