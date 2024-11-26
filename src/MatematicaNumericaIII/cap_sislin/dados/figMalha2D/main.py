import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
  "text.usetex": True,
  "font.family": "Computer Modern Serif",
  "font.size"  : 10
})

fig, ax = plt.subplots(dpi=200)
ax.axis("off")
ax.set_aspect("equal")

plt.arrow(-1,-1,0.5,0,head_width=0.1,color="black")
plt.text(-0.3,-1.1,"$x$")

plt.arrow(-1,-1,0,0.5,head_width=0.1,color="black")
plt.text(-0.9,-0.4,"$y$")

for i in np.arange(7):
  plt.plot(2*[i], [0,6],color="black",lw=0.1)
  plt.plot(7*[i], np.arange(7), ls="", lw=0.1,
           marker="o", markersize=2, color="black",)
for j in np.arange(7):
  plt.plot([0,6],2*[j],color="black",lw=0.1)

plt.plot([3],[3],marker="o",markersize=4,color="black")
plt.plot([3],[2],marker="o",markersize=4,color="red")
plt.plot([3],[4],marker="o",markersize=4,color="red")
plt.plot([2],[3],marker="o",markersize=4,color="red")
plt.plot([4],[3],marker="o",markersize=4,color="red")
  
for i,v in enumerate(["$1$","$2$","$3$","$i$","$n-2$","$n-1$","$n$"]):
  plt.text(i,-0.3,v)

plt.text(-0.2,0,"$1$")
plt.text(-0.2,1,"$2$")
plt.text(-0.2,2,"$3$")
plt.text(-0.2,3,"$j$")
plt.text(-0.735,4,"$n-2$")
plt.text(-0.735,5,"$n-1$")
plt.text(-0.25,6,"$n$")

plt.text(1.1,1.2,"$1$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(2.1,1.2,"$2$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(3.1,1.2,"$\\cdots$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(4.1,1.2,"$n-3$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(5.1,1.2,"$n-2$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))

plt.text(1.1,2.2,"$(n-2)+1$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(3.1,2.2,"$\\cdots$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(4.1,2.2,"$\\cdots$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(5.1,2.2,"$2(n-2)$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))

plt.annotate("$(j-2)(n-2)+1$", xy=(0.95,3.1), xytext=(-1.5,3.5),
             bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4),
             arrowprops=dict(facecolor='black', width=0.01,
                             headwidth=2, headlength=3))

plt.annotate("$i-1+(j-2)(n-2)$", xy=(3.025,3.1), xytext=(1.75,3.5),
             bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4),
             arrowprops=dict(facecolor='black', width=0.01,
                             headwidth=2, headlength=3))

plt.annotate("$(j-1)(n-2)$", xy=(5.1,3.075), xytext=(5.5,3.5),
             bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4),
             arrowprops=dict(facecolor='black', width=0.01,
                             headwidth=2, headlength=3))

plt.text(1.1,4.2,"$\\cdots$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(2.1,4.2,"$\\cdots$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(3.1,4.2,"$\\cdots$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(4.1,4.2,"$\\cdots$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(5.1,4.2,"$\\cdots$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))

plt.text(1.1,5.2,"$(n-3)(n-2)$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(4.1,5.2,"$\\cdots$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(5.1,5.2,"$(n-2)(n-2)$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))


plt.savefig('fig.png', bbox_inches='tight')
