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
ax.set_xlim((-1.1,6.5))
ax.set_ylim((-1.1,6.5))

plt.arrow(-1,-1,0.5,0,head_width=0.1,color="black")
plt.text(-0.3,-1.1,"$x$")

plt.arrow(-1,-1,0,0.5,head_width=0.1,color="black")
plt.text(-0.9,-0.4,"$y$")

for i in np.arange(7):
  plt.plot(2*[i], [0,6],color="black",lw=0.1)
for j in np.arange(7):
  plt.plot([0,6],2*[j],color="black",lw=0.1)

for i in range(7):
  for j in range(7):
    c = "red"
    if ((i==0) or (i==6)):
      if (j==0):
        c = "black"
      elif (j<6):
        c = "blue"
      else:
        c = "black"
    if ((j==0) or (j==6)):
      if (i==0):
        c = "black"
      elif (i<6):
        c = "blue"
      else:
        c = "black"
        
    plt.plot([i], [j], ls="", lw=0.1,
             marker="o", markersize=2, color=c,)

  
for i,v in enumerate(["$1$","$2$","$3$","$i$","$n_x-1$","$n_x$","$n_x+1$"]):
  plt.text(i,-0.3,v)

plt.text(-0.2,0,"$1$")
plt.text(-0.2,1,"$2$")
plt.text(-0.2,2,"$3$")
plt.text(-0.2,3,"$j$")
plt.text(-0.785,4,"$n_y-1$")
plt.text(-0.4,5,"$n_y$")
plt.text(-0.785,6,"$n_y+1$")

plt.text(0.05,0.1,"$(a,c)$")
plt.text(6.1-0.65,0.1,"$(b,c)$")
plt.text(0.05,6.2-0.45,"$(a,d)$")
plt.text(6.1-0.65,6.2-0.45,"$(b,d)$")

plt.text(0.4,0.4,"$C_1$")
plt.text(1.4,0.4,"$C_2$")
plt.text(2.4,0.4,"$\\cdots$")
plt.text(2.4,0.4,"$\\cdots$")
plt.text(4.4,0.4,"$\\cdots$")
plt.text(5.4,0.4,"$C_{n_x}$")

plt.text(0.3,1.4,"$C_{n_x+1}$")
plt.text(1.4,1.4,"$\\cdots$")
plt.text(4.4,1.4,"$\\cdots$")
plt.text(5.3,1.4,"$C_{2n_x}$")

plt.text(0.5,2.4,"$\\vdots$")
plt.text(5.5,2.4,"$\\vdots$")

plt.text(0.5,4.4,"$\\vdots$")
plt.text(5.5,4.4,"$\\vdots$")

plt.text(0.4,5.4,"$\\cdots$")
plt.text(5.3,5.4,"$C_{n_xn_y}$")

plt.savefig('fig.png', bbox_inches='tight')
plt.close()
