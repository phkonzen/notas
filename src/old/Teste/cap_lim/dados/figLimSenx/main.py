import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches


plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

fig, ax = plt.subplots()

x = np.pi/4

ax.axis('off')
ax.set_xlim(-0.2,1+0.2)
ax.set_ylim(-0.2,np.sin(x)+0.2)
ax.set_aspect(1.)


ax.plot([0,1],[0,0],lw="3",color="blue")
ax.plot([0,1],[0,0],lw="1",color="red")

ax.plot([0,np.cos(x)],[0, np.sin(x)],lw="3",color="blue")
ax.plot([0,np.cos(x)],[0, np.sin(x)],lw="1",color="red")

ax.plot([1,np.cos(x)],[0,np.sin(x)],lw="3",color="blue")

ax.plot([np.cos(x),np.cos(x)],[0,np.sin(x)],ls="--",color="gray")

arc = patches.Arc((0,0), 2, height=2, theta1=0.0, theta2=45,
                  lw=1, color="red")
ax.add_patch(arc)

ax.text(-0.1,-0.075,"$O=(0,0)$")
ax.text(1-0.1,-0.075,"$A=(1,0)$")
ax.text(np.cos(x)-0.15,np.sin(x)+0.05,"$P=(\\cos(x),\\mathrm{sen}(x))$")

fig.savefig('fig.png', bbox_inches='tight')


