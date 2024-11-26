import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
  "text.usetex": True,
  "font.family": "Computer Modern Serif",
  "font.size"  : 12
})

fig, ax = plt.subplots(dpi=200)
ax.axis("off")
ax.set_aspect("equal")

plt.arrow(-1,-1,0.5,0,head_width=0.1,color="black")
plt.text(-0.3,-1.1,"$x$")

plt.arrow(-1,-1,0,0.5,head_width=0.1,color="black")
plt.text(-0.9,-0.4,"$y$")

for i in np.arange(5):
  plt.plot(2*[i], [0,4],color="black",lw=0.1)
for j in np.arange(5):
  plt.plot([0,4],2*[j],color="black",lw=0.1)

plt.plot([0],[0],marker="o",color="black")
plt.text(0,-0.3,"1")
plt.plot([1],[0],marker="o",color="black")
plt.text(1,-0.3,"2")
plt.text(2,0,"$\cdots$",fontsize=20)
plt.text(2,-0.3,"$i$")
plt.plot([3],[0],marker="o",color="black")
plt.text(3,-0.3,"$n-1$")
plt.plot([4],[0],marker="o",color="black")
plt.text(4,-0.3,"$n$")

plt.plot([0],[1],marker="o",color="black")
plt.plot([1],[1],marker="o",color="black")
plt.text(2,1,"$\\cdots$",fontsize=20)
plt.plot([3],[1],marker="o",color="black")
plt.plot([4],[1],marker="o",color="black")

plt.text(0,2,"$\\vdots$",fontsize=24)
plt.text(1,2,"$\\vdots$",fontsize=24)
plt.text(3,2,"$\\vdots$",fontsize=24)
plt.text(4,2,"$\\vdots$",fontsize=24)

plt.plot([0],[3],marker="o",color="black")
plt.plot([1],[3],marker="o",color="black")
plt.text(2,3,"$\\cdots$",fontsize=20)
plt.plot([3],[3],marker="o",color="black")
plt.plot([4],[3],marker="o",color="black")

plt.plot([0],[4],marker="o",color="black")
plt.plot([1],[4],marker="o",color="black")
plt.text(2,4,"$\\cdots$",fontsize=20)
plt.plot([3],[4],marker="o",color="black")
plt.plot([4],[4],marker="o",color="black")

plt.text(-0.25,0,"1")
plt.text(-0.25,1,"2")
plt.text(-0.25,2,"$j$")
plt.text(-0.675,3,"$n-1$")
plt.text(-0.25,4,"$n$")

plt.text(0.1,0.2,"$1$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.5))
plt.text(1.1,0.2,"$2$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.5))
plt.text(3.1,0.2,"$n-1$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.5))
plt.text(4.1,0.2,"$n$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.5))

plt.text(0.1,1.2,"$n+1$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.5))
plt.text(1.1,1.2,"$n+2$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.5))
plt.text(3.1,1.2,"$2n-1$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.5))
plt.text(4.1,1.2,"$2n$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.5))

plt.text(1.4,2.2,"$i+j(n-1)$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.5))

plt.text(0.1,3.2,"$(j-1)n+1$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.5))
#plt.text(1.1,3.2,"$\\cdots$",
#         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.5))
plt.text(3.1,3.2,"$\\cdots$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.5))
plt.text(4.1,3.2,"$jn$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.5))

plt.text(0.1,4.2,"$(n-1)n+1$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.5))
#plt.text(1.1,4.2,"$(n-2)n$",
#         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.5))
plt.text(3.1,4.2,"$\\cdots$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.5))
plt.text(4.1,4.2,"$n^2$",
         bbox=dict(boxstyle="Round,pad=0.2",fc="white",lw=0.5))

plt.savefig('full.png', bbox_inches='tight')
