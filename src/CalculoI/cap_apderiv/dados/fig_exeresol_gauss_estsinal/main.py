#!/bin/python3

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(4,1),frameon=False)
ax = plt.subplot(1,1,1)
plt.axis('off')
ax.set_ylim((0.5,4))
ax.set_xlim((-1,1))

ax.plot([-1,1],[3,3],color="black")
ax.plot([-1,1],[2,2],color="black")
ax.plot([-1,1],[1,1],color="black")
ax.plot([0,0],[0.9,3.1],ls="--",color="gray")
ax.text(0,2.2,"$0$")
ax.text(0,0.5,"$0$")

ax.text(1+0.025,3,"$-2x$",fontsize=12)
ax.text(-0.5,3+0.1,"$+$",fontsize=12,color="black")
ax.text(0.5,3+0.1,"$-$",fontsize=12,color="black")

ax.text(1+0.025,2,"$e^x$",fontsize=12)
ax.text(-0.5,2+0.1,"$+$",fontsize=12,color="black")
ax.text(0.5,2+0.1,"$+$",fontsize=12,color="black")

ax.text(1+0.025,1,"f'(x)",fontsize=12)
ax.text(-0.5,1+0.1,"$+$",fontsize=12,color="red")
ax.text(0.5,1+0.1,"$-$",fontsize=12,color="blue")

fig.savefig('fig_exeresol_gauss_estsinal.png', bbox_inches="tight")





