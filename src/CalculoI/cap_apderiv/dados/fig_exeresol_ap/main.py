import numpy as np
import matplotlib.pyplot as plt
from sympy import *

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

fig, ax = plt.subplots()

ax.plot([0.2,0.8],[1,1],ls='-',color='black')
ax.plot([0.2,0.2],[0.5,1],ls='-',color='black')
ax.plot([0.8,0.8],[0.5,1],ls='-',color='black')
ax.plot([0.2,0.8],[0.5,0.5],ls='-',color='black')

ax.text(0.45,1.025,'\$ 2/metro')
ax.text(0.35,0.75,'Área 1 km$^2$')
ax.text(0.15,0.75,'$x$')
ax.text(0.825,0.75,'$x$')
ax.text(0.475,0.45,'$y$')

ax.set_aspect('equal')
ax.set_axis_off()

fig.savefig('fig.png', bbox_inches='tight')
