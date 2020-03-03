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

ax.set_xlim((-3,3))
ax.set_ylim((-3,6))

p=1
x = np.linspace(-3,3, 400)
ax.plot(x,x**2/(2*p))

ax.arrow(-3,0,6,0,color='black',
         length_includes_head=True,head_width=0.1)
ax.text(3,0-0.3,'$x$')
ax.arrow(0,-3,0,9,color='black',
         length_includes_head=True,head_width=0.1)
ax.text(0+0.2,6-0.2,'$y$')

ax.plot(x,-(p/2)*np.ones(np.size(x)),color='red')
ax.text(3,-(p/2)-0.3,'$d$')

ax.plot([0],[p/2],marker='o',markersize=3,color='red')
ax.text(0-0.4,p/2,'$F$')

x0=2
ax.plot(x0,x0**2/(2*p),marker='o',markersize=3,color='black')
ax.text(x0-0.4,x0**2/(2*p),'$P$')
ax.plot([0,x0],[p/2,x0**2/(2*p)],ls='--',color='gray')
ax.plot([x0,x0,],[-p/2,x0**2/(2*p)],ls='--',color='gray')

# vertice
ax.plot([0],[0],color='black',marker='o',markersize=3)


fig.savefig("fig_parabola.png", bbox_inches="tight")
