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

x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
x, y = np.meshgrid(x, y)

a=1.5
b=2
ax.contour(x,y,(x**2/a**2-y**2/b**2),[1],colors='blue')

ax.arrow(-5,0,10,0,length_includes_head=True,head_width=0.1)
ax.arrow(0,-5,0,10,length_includes_head=True,head_width=0.1)

ax.text(-a+0.25,0+0.1,'$A_1$')
ax.plot([-a],[0],marker='o',markersize=4,color='blue')
ax.text(a-0.75,0+0.1,'$A_2$')
ax.plot([a],[0],marker='o',markersize=4,color='blue')

ax.text(0-0.75,-b-0.5,'$B_2$')
ax.plot([0],[-b],marker='o',markersize=4,color='blue')
ax.text(0-0.75,b+0.1,'$B_1$')
ax.plot([0],[b],marker='o',markersize=4,color='blue')

c = np.sqrt(a**2+b**2)
ax.text(-c-0.75,0+0.1,'$F_1$')
ax.plot([-c],[0],marker='o',markersize=4,color='blue')
ax.text(c+0.25,0+0.1,'$F_2$')
ax.plot([c],[0],marker='o',markersize=4,color='blue')

Py = 2
Px = np.sqrt(a**2*(1 + Py**2/b**2))
ax.text(Px+0.15,Py+0.15,'$P$')
ax.plot([Px],[Py],marker='o',markersize=4,color='blue')

ax.plot([-c,Px],[0,Py],ls='--',color='black')
ax.plot([c,Px],[0,Py],ls='--',color='black')

ax.plot([-a,-a],[-b,b],ls='--',color="gray")
ax.plot([a,a],[-b,b],ls='--',color="gray")
ax.plot([-a,a],[-b,-b],ls='--',color="gray")
ax.plot([-a,a],[b,b],ls='--',color="gray")

x = np.linspace(-5, 5, 400)
y = b/a*x
ax.plot(x,y,ls='--',color='gray')
y= -b/a*x
ax.plot(x,y,ls='--',color='gray')

fig.savefig("fig_hiperbole.png", bbox_inches="tight")
