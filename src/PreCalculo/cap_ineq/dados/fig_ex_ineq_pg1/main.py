import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 12,
    'text.latex.preamble': r'\usepackage{amsfonts}'
})

fig, ax = plt.subplots()
fig.set_size_inches(6.4,2.05)
ax.axis("off")
ax.set_xlim((-4.25,4.25))
ax.set_ylim((-4,8))

ax.text(-1.85,7,"$1$")
ax.text(2.15,7,"$2$")

ax.text(-4,7,"$x-1$")

ax.plot([-2,-2],[-2,7.5],ls="--",color="gray")

ax.arrow(-2,6,6,0,
         length_includes_head=True,
         head_width = 0.5,
         head_length = 0.1,
         overhang=1.0, color="blue")
ax.arrow(-2,6,-2,0,
         length_includes_head=True,
         head_width = 0.5,
         head_length = 0.1,
         overhang=1.0, color="red")

ax.plot([-2],[6],color="black",marker="o",mfc="white")

ax.text(-3,7.25,"$-$",fontsize=14)
ax.text(0,6.75,"$+$",fontsize=14)
ax.text(3,6.75,"$+$",fontsize=14)

ax.text(-4,4,"$2-x$")

ax.plot([2,2],[-2,7.5],ls="--",color="gray")

ax.arrow(2,3,2,0,
         length_includes_head=True,
         head_width = 0.5,
         head_length = 0.1,
         overhang=1.0, color="red")
ax.arrow(2,3,-6,0,
         length_includes_head=True,
         head_width = 0.5,
         head_length = 0.1,
         overhang=1.0, color="blue")

ax.plot([2],[3],color="black",marker="o",mfc="white")

ax.text(-3,3.75,"$+$",fontsize=14)
ax.text(0,3.75,"$+$",fontsize=14)
ax.text(3,4.25,"$-$",fontsize=14)

ax.text(-4,1,"$\\times$")

ax.text(-3,1.25,"$-$",fontsize=14)
ax.text(0,0.75,"$+$",fontsize=14)
ax.text(3,1.25,"$-$",fontsize=14)

ax.plot([-2],[0],color="black",marker="o",mfc="white")
ax.plot([2],[0],color="black",marker="o",mfc="white")

ax.arrow(2,0,2,0,
         length_includes_head=True,
         head_width = 0.5,
         head_length = 0.1,
         overhang=1.0, color="red")
ax.arrow(-2,0,4,0,
         length_includes_head=True,
         head_width = 0.5,
         head_length = 0.,
         overhang=1.0, color="blue")
ax.arrow(-2,0,-2,0,
         length_includes_head=True,
         head_width = 0.5,
         head_length = 0.1,
         overhang=1.0, color="red")

ax.text(-1.85,-1.25,"$1$")
ax.text(2.15,-1.25,"$2$")


plt.savefig("fig.png", bbox_inches='tight', pad_inches=0)
