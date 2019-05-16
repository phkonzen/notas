from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
#font letter
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=12)

#figure
fig = plt.figure(figsize=(6,6), dpi=300, 
                 linewidth=0.0, facecolor="white")
ax = fig.gca(projection='3d')
ax.axis('on')
ax.set_xlabel('$x$')
# ax.set_xticks([-2,-1,0,1,2,3])
ax.set_ylabel('$y$')
# ax.set_yticks([-2,-1,0,1,2])
ax.set_zlabel('$z$')
# ax.set_zticks([-2,-1,0,1,2,3,4])

lbda = np.linspace(-1.5,2.25)
x = -1 + 2*lbda
y = 2 + 3*lbda
z = 1 - 2*lbda
plt.plot(x,y,z,color='black')
plt.plot([-1],[2],[1],marker='o',color='black')
ax.text(-1,2,1.25,'$A=(-1,2,1)$')
plt.plot([1],[5],[-1],marker='o',color='black')
ax.text(1,5,-0.75,'$B=(1,5,-1)$')

fig.savefig("fig_exeresol_er_sim.pdf", bbox_inches="tight")
