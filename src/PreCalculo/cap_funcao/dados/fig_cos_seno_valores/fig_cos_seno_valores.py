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

ax.text(-0.1,-0.15,'$0$')
ax.text(1.05,-0.15,'$1$')

ax.text(-1.175,-0.15,'$-1$')
ax.text(-0.175,-1.125,'$-1$')
ax.text(-0.08,1.05,'$1$')

ax.plot([1/2,1/2],[-np.sin(np.pi/3),np.sin(np.pi/3)],color='gray',ls='--')
ax.plot([np.sqrt(2)/2,np.sqrt(2)/2],[-np.sin(np.pi/4),np.sin(np.pi/4)],color='gray',ls='--')
ax.plot([np.sqrt(3)/2,np.sqrt(3)/2],[-np.sin(np.pi/6),np.sin(np.pi/6)],color='gray',ls='--')

ax.plot([-1/2,-1/2],[-np.sin(np.pi/3),np.sin(np.pi/3)],color='gray',ls='--')
ax.plot([-np.sqrt(2)/2,-np.sqrt(2)/2],[-np.sin(np.pi/4),np.sin(np.pi/4)],color='gray',ls='--')
ax.plot([-np.sqrt(3)/2,-np.sqrt(3)/2],[-np.sin(np.pi/6),np.sin(np.pi/6)],color='gray',ls='--')

ax.plot([-np.cos(np.pi/6),np.cos(np.pi/6)],[1/2,1/2],color='gray',ls='--')
ax.plot([-np.cos(np.pi/4),np.cos(np.pi/4)],[np.sqrt(2)/2,np.sqrt(2)/2],color='gray',ls='--')
ax.plot([-np.cos(np.pi/3),np.cos(np.pi/3)],[np.sqrt(3)/2,np.sqrt(3)/2],color='gray',ls='--')

ax.plot([-np.cos(np.pi/6),np.cos(np.pi/6)],[-1/2,-1/2],color='gray',ls='--')
ax.plot([-np.cos(np.pi/4),np.cos(np.pi/4)],[-np.sqrt(2)/2,-np.sqrt(2)/2],color='gray',ls='--')
ax.plot([-np.cos(np.pi/3),np.cos(np.pi/3)],[-np.sqrt(3)/2,-np.sqrt(3)/2],color='gray',ls='--')

ax.text(1/2-0.1,-0.2,'$\\frac{1}{2}$',
        bbox=dict(facecolor='white', edgecolor='none',alpha=0.7))
ax.text(np.sqrt(2)/2-0.1,-0.2,'$\\frac{\\sqrt{2}}{2}$',
        bbox=dict(facecolor='white', edgecolor='none',alpha=0.7))
ax.text(np.sqrt(3)/2-0.1,-0.2,'$\\frac{\\sqrt{3}}{2}$',
        bbox=dict(facecolor='white', edgecolor='none',alpha=0.7))
ax.text(-0.1,1/2-0.15,'$\\frac{1}{2}$',
        bbox=dict(facecolor='white', edgecolor='none',alpha=0.7))
ax.text(-0.15,np.sqrt(2)/2-0.15,'$\\frac{\\sqrt{2}}{2}$',
        bbox=dict(facecolor='white', edgecolor='none',alpha=0.7))
ax.text(-0.15,np.sqrt(3)/2-0.1,'$\\frac{\\sqrt{3}}{2}$',
        bbox=dict(facecolor='white', edgecolor='none',alpha=0.7))

ax.text(1+0.02,0+0.025,'$0$')

ax.text(np.cos(np.pi/6)+0.02,np.sin(np.pi/6),'$\\frac{\\pi}{6}$')
ax.text(np.cos(np.pi/4)+0.02,np.sin(np.pi/4),'$\\frac{\\pi}{4}$')
ax.text(np.cos(2*np.pi/6)+0.02,np.sin(2*np.pi/6),'$\\frac{2\\pi}{6}$')

ax.text(0+0.05,1+0.05,'$\\frac{\\pi}{2}$')

ax.text(np.cos(4*np.pi/6)-0.125,np.sin(4*np.pi/6),'$\\frac{4\\pi}{6}$')
ax.text(np.cos(3*np.pi/4)-0.125,np.sin(3*np.pi/4),'$\\frac{3\\pi}{4}$')
ax.text(np.cos(5*np.pi/6)-0.125,np.sin(5*np.pi/6),'$\\frac{5\\pi}{6}$')

ax.text(-1-0.11,0+0.025,'$\\pi$')

ax.text(np.cos(7*np.pi/6)-0.125,np.sin(7*np.pi/6)-0.125,'$\\frac{7\\pi}{6}$')
ax.text(np.cos(5*np.pi/4)-0.125,np.sin(5*np.pi/4)-0.125,'$\\frac{5\\pi}{4}$')
ax.text(np.cos(8*np.pi/6)-0.125,np.sin(8*np.pi/6)-0.125,'$\\frac{8\\pi}{6}$')

ax.text(0+0.05,-1-0.175,'$\\frac{3\\pi}{2}$')

ax.text(np.cos(10*np.pi/6)+0.05,np.sin(10*np.pi/6)-0.125,'$\\frac{10\\pi}{6}$')
ax.text(np.cos(7*np.pi/4)+0.05,np.sin(7*np.pi/4)-0.125,'$\\frac{7\\pi}{4}$')
ax.text(np.cos(11*np.pi/6)+0.05,np.sin(11*np.pi/6)-0.125,'$\\frac{11\\pi}{6}$')


plt.savefig('fig_cos_seno_valores.png',bbox_inches='tight')

