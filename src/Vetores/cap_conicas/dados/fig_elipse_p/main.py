#!/usr/bin/python3
'''
Pedro H A Konzen - UFRGS - 2019
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches

#font letter
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=12)

#figure
fig = plt.figure(figsize=(4,4), dpi=100, 
                 linewidth=0.0, facecolor="white")
ax = plt.subplot(1,1,1)
ax.axis('off')

ax.set_xlim((-5,5.5))
ax.set_ylim((-5,5.5))

ellipse = patches.Ellipse((0,0),8,6,
                          edgecolor='blue', facecolor='none')
ax.add_patch(ellipse)
ax.arrow(-5,0,10,0,length_includes_head=True,head_width=0.1)
ax.arrow(0,-5,0,10,length_includes_head=True,head_width=0.1)

ax.text(-4-0.75,0+0.1,'$A_1$')
ax.plot([-4],[0],marker='o',markersize=4,color='blue')
ax.text(4,0+0.1,'$A_2$')
ax.plot([4],[0],marker='o',markersize=4,color='blue')

ax.text(0-0.75,-3-0.5,'$B_2$')
ax.plot([0],[-3],marker='o',markersize=4,color='blue')
ax.text(0-0.75,3+0.1,'$B_1$')
ax.plot([0],[3],marker='o',markersize=4,color='blue')

ax.text(-np.sqrt(7)-0.75,0+0.1,'$F_1$')
ax.plot([-np.sqrt(7)],[0],marker='o',markersize=4,color='blue')
ax.text(np.sqrt(7)-0.75,0+0.1,'$F_2$')
ax.plot([np.sqrt(7)],[0],marker='o',markersize=4,color='blue')

ax.text(-np.sqrt(7)/2,-0.5,'$c$')
ax.text(np.sqrt(7)/2,-0.5,'$c$')


ax.text(2+0.15,3/2*np.sqrt(3)+0.15,'$P$')
ax.plot([2],[3/2*np.sqrt(3)],marker='o',markersize=4,color='blue')

ax.plot([-np.sqrt(7),2],[0,3/2*np.sqrt(3)],ls='--',color='black')
ax.plot([np.sqrt(7),2],[0,3/2*np.sqrt(3)],ls='--',color='black')

fig.savefig("fig_elipse_p.png", bbox_inches="tight")
