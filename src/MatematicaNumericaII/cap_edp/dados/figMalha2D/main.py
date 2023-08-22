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
plt.text(-0.3,-1.1,"$i, x$")

plt.arrow(-1,-1,0,0.5,head_width=0.1,color="black")
plt.text(-0.9,-0.4,"$j, y$")

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
  
for i,v in enumerate(["$1$","$2$","$3$","$i$","$n-1$","$n$","$n+1$"]):
  plt.text(i,-0.3,v)

plt.text(-0.2,0,"$1$")
plt.text(-0.2,1,"$2$")
plt.text(-0.2,2,"$3$")
plt.text(-0.2,3,"$j$")
plt.text(-0.735,4,"$n-1$")
plt.text(-0.735,5,"$n$")
plt.text(-0.25,6,"$n+1$")

plt.text(0.1,0.2,"$1$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(1.1,0.2,"$2$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(2.1,0.2,"$3$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(3.1,0.2,"$\\cdots$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(5.1,0.2,"$n$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(6.1,0.2,"$n+1$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))

plt.text(0.1,1.2,"$n+2$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(3.1,1.2,"$\\cdots$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(6.1,1.2,"$2(n+1)$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))

plt.text(0.1,3.2,"$\\vdots$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(6.1,3.2,"$\\vdots$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))

plt.text(3.1,2.2,"$k-n-1$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(2.1,3.2,"$k-1$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(3.1,3.2,"$k$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(4.1,3.2,"$k+1$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(3.1,4.2,"$k+n+1$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))

plt.text(6.1,3.2,"$\\vdots$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))

plt.text(0.1,6.2,"$n(n+1)$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(3.1,6.2,"$\\cdots$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))
plt.text(6.1,6.2,"$(n+1)^2$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.4))


plt.savefig('fig.png', bbox_inches='tight')
plt.savefig('fig.pdf', bbox_inches='tight')
