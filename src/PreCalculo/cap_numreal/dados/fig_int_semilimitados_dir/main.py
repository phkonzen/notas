import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 12,
    'text.latex.preamble': r'\usepackage{amsfonts}'
})

fig, ax = plt.subplots()
fig.set_size_inches(6.4,2.1)
ax.axis("off")
ax.set_xlim((-4,4))
ax.set_ylim((-1,1))

ax.arrow(0,0.5,4,0,
         lw=0.1,
         length_includes_head=True,
         head_width = 0.1,
         head_length = 0.1,
         overhang=1.0)

ax.arrow(0,0.5,-4,0,
         lw=0.1,
         length_includes_head=True,
         head_width = 0.1,
         head_length = 0.1,
         overhang=1.0)

ax.arrow(1,0.5,-6,0,
         lw=0.5,
         length_includes_head=True,
         head_width = 0.1,
         head_length = 0.1,
         overhang=1.0,
         color="blue")

ax.plot([1],[0.5],ls='',marker='o',markersize=5,color='blue',
        markerfacecolor='blue')
ax.text(1-0.1, 0.3, "b")

ax.arrow(0,-0.5,4,0,
         lw=0.1,
         length_includes_head=True,
         head_width = 0.1,
         head_length = 0.1,
         overhang=1.0)

ax.arrow(0,-0.5,-4,0,
         lw=0.1,
         length_includes_head=True,
         head_width = 0.1,
         head_length = 0.1,
         overhang=1.0)

ax.arrow(1,-0.5,-6,0,
         lw=0.5,
         length_includes_head=True,
         head_width = 0.1,
         head_length = 0.1,
         overhang=1.0,
         color="blue")

ax.plot([1],[-0.5],ls='',marker='o',markersize=5,color='blue',
        markerfacecolor='white')
ax.text(1-0.1, -0.7, "b")

#ax.plot([2],[0.5],ls='',marker='o',markersize=5,color='blue',
#        markerfacecolor='white')
#ax.text(2, 0.4, "b")


plt.savefig("main.png", bbox_inches='tight', pad_inches=0)
