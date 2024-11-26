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
  lw = 0.1
  if (i%2 == 0):
    lw = 0.2
  plt.plot(2*[i], [0,6],color="black",lw=lw)
for j in np.arange(7):
  lw = 0.1
  if (j%2 == 0):
    lw = 0.2
  plt.plot([0,6],2*[j],color="black",lw=lw)

nx = 6
ny = 6
# 1
plt.plot([0], [0], ls="", lw=0.1,
         marker="o", markersize=2, color="black")
plt.plot([nx], [0], ls="", lw=0.1,
         marker="o", markersize=2, color="black")
plt.plot([0], [ny], ls="", lw=0.1,
         marker="o", markersize=2, color="black")
plt.plot([nx], [ny], ls="", lw=0.1,
         marker="o", markersize=2, color="black")
# 2
for i in range(1,nx//2):
  plt.plot([2*i], [0], ls="", lw=0.1,
         marker="v", markersize=2, color="blue")
  plt.plot([2*i], [ny], ls="", lw=0.1,
         marker="v", markersize=2, color="blue")
for j in range(1,ny//2):
  plt.plot([0], [2*j], ls="", lw=0.1,
         marker="v", markersize=2, color="blue")
  plt.plot([nx], [2*j], ls="", lw=0.1,
         marker="v", markersize=2, color="blue")
# 4
for i in range(1,nx//2+1):
  plt.plot([2*i-1], [0], ls="", lw=0.1,
         marker="^", markersize=2, color="red")
  plt.plot([2*i-1], [ny], ls="", lw=0.1,
         marker="^", markersize=2, color="red")
for j in range(1,ny//2+1):
  plt.plot([0], [2*j-1], ls="", lw=0.1,
         marker="^", markersize=2, color="red")
  plt.plot([nx], [2*j-1], ls="", lw=0.1,
         marker="^", markersize=2, color="red")
for i in range(1,nx//2):
  for j in range(1,ny//2):
    plt.plot([2*i], [2*j], ls="", lw=0.1,
             marker="^", markersize=2, color="red")
# 8
for i in range(1,nx//2):
  for j in range(1,ny//2+1):
    plt.plot([2*i], [2*j-1], ls="", lw=0.1,
         marker="D", markersize=2, color="gray")
for i in range(1,ny//2+1):
  for j in range(1,ny//2):
    plt.plot([2*i-1], [2*j], ls="", lw=0.1,
         marker="D", markersize=2, color="gray")
    
# 16
for i in range(1,nx//2+1):
  for j in range(1,ny//2+1):
    plt.plot([2*i-1], [2*j-1], ls="", lw=0.1,
             marker="P", markersize=3, color="green")

  
for i,v in enumerate(["$1$","$2$","$3$","$i$","$n_x-1$","$n_x$","$n_x+1$"]):
  plt.text(i,-0.3,v)

plt.text(-0.25,0,"$1$")
plt.text(-0.25,1,"$2$")
plt.text(-0.25,2,"$3$")
plt.text(-0.25,3,"$j$")
plt.text(-0.79,4,"$n_y-1$")
plt.text(-0.45,5,"$n_y$")
plt.text(-0.79,6,"$n_y+1$")

plt.text(-0.6,-0.25,"$(a,c)$")
plt.text(6.1,0.1,"$(b,c)$")
plt.text(0.05,6.1,"$(a,d)$")
plt.text(6.1,6.1,"$(b,d)$")

plt.text(1.1,1.1,"$C_1$")
plt.text(3.1,1.1,"$\\cdots$")
plt.text(5.1,1.1,"$C_{n_x/2}$")

plt.text(1.1,3.1,"$\\vdots$")
plt.text(5.1,3.1,"$\\vdots$")

plt.text(1.1,5.1,"$\\cdots$")
plt.text(5.1,5.1,"$C_{n_xn_y/4}$")

plt.savefig('fig.png', bbox_inches='tight')
plt.close()
