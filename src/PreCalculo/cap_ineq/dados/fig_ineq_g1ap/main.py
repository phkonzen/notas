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
         overhang=1.0, color="blue")
ax.arrow(0,0,-4,0,
         length_includes_head=True,
         head_width = 0.025,
         head_length = 0.1,
         overhang=1.0, color="red")

ax.plot([0],[0],color="black",marker="o",mfc="white")
ax.text(0, -0.1, "$-\\frac{b}{a}$")

ax.text(-2, -0.045, "$-$", color="red", fontsize=14)
ax.text(2, 0.035, "$+$", color="blue", fontsize=14)

plt.savefig("fig.png", bbox_inches='tight', pad_inches=0)
