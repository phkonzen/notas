import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('font', size=12)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.axis('off')
ax.set_xlim((-1.75,1.75))
ax.set_ylim((-1.35,1.35))

ax.arrow(-1.35,0,2.7,0,head_width=0.05,
         length_includes_head=True)
ax.text(1.35,-0.1,"cos")
ax.arrow(0,-1.35,0,2.7,head_width=0.05,
         length_includes_head=True)
ax.text(-0.25,1.25,"sen")

circle = plt.Circle((0,0),1,facecolor='none',edgecolor='blue')
ax.add_artist(circle)

a = 1.5*np.pi/6
plt.plot([0,np.cos(a)],[0,np.sin(a)],color='black')
ax.add_patch(Arc((0,0),0.4,0.4,theta1=0,theta2=a*180/np.pi,edgecolor='k'))
ax.text(0.25,0.1,"$x$")

ax.plot([-0.025,np.cos(a)],[np.sin(a),np.sin(a)],ls='--',color='gray')
ax.text(-0.4,np.sin(a),'$\mathrm{sen}(x)$')
ax.plot([np.cos(a),np.cos(a)],[-0.025,np.sin(a)],ls='--',color='gray')
ax.text(np.cos(a)-0.15,-0.15,'$\mathrm{cos}(x)$')

a = 8*np.pi/6
plt.plot([0,np.cos(a)],[0,np.sin(a)],color='black')
ax.add_patch(Arc((0,0),0.2,0.2,theta1=0,theta2=a*180/np.pi,edgecolor='k'))
ax.text(-0.225,-0.125,"$x'$")

ax.plot([0.025,np.cos(a)],[np.sin(a),np.sin(a)],ls='--',color='gray')
ax.text(0.05,np.sin(a),"$\mathrm{sen}(x')$")
ax.plot([np.cos(a),np.cos(a)],[0.025,np.sin(a)],ls='--',color='gray')
ax.text(np.cos(a)-0.15,0.1,"$\mathrm{cos}(x')$")

ax.text(0.05,-0.15,'$0$')
ax.text(1.05,-0.15,'$1$')
ax.text(-1.175,-0.15,'$-1$')
ax.text(-0.175,-1.125,'$-1$')
ax.text(-0.08,1.05,'$1$')

plt.savefig('fig_seno_cosseno.png',bbox_inches='tight')

