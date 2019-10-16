#!/bin/python3

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(4,1),frameon=False)
ax = plt.subplot(1,1,1)
plt.axis('off')
ax.set_ylim((0.5,2))
ax.set_xlim((-0.25,3))
ax.plot([-0.25,3],[1,1],color="black")
ax.text(3+0.025,1,"$f'(x)$",fontsize=12)

x1 = (4 - np.sqrt(7))/3
x2 = (4 + np.sqrt(7))/3
ax.plot([x1,x1],[0.9,1.1],color="black")
ax.plot([x2,x2],[0.9,1.1],color="black")

ax.text(0,1+0.1,"$+$",fontsize=12,color="blue")
ax.text(1.25,1+0.1,"$-$",fontsize=12,color="red")
ax.text(2.5,1+0.1,"$+$",fontsize=12,color="blue")
fig.savefig('fig_ex_monoderiv_poli.png', bbox_inches="tight")





