#!/usr/bin/python3

'''
import matplotlib as mpl
mpl.use("pgf")
pgf_with_rc_fonts = {
    "font.family": "serif",
    "font.serif": [],                   # use latex default serif font
    "font.sans-serif": ["DejaVu Sans"], # use a specific sans-serif font
    "font.size": 12,
}
mpl.rcParams.update(pgf_with_rc_fonts)
'''

import matplotlib.pyplot as plt
import numpy as np

#font letter
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=12)


fig = plt.figure(figsize=(5,2), dpi=300, linewidth=0.0, facecolor="white")
ax1 = plt.subplot(1,1,1)

ax1.axis('off')
ax1.set_xlim((-0.3,12))
ax1.set_ylim((-0.3,1.75))

#x-axis
ax1.arrow(0,0, 12, 0, length_includes_head=True,
          head_width=0.1)
ax1.text(11.5,-0.25,"$x$")

#y-axis
ax1.arrow(0,0, 0, 1.75, length_includes_head=True,
          head_width=0.125, head_length=0.1)
ax1.text(-0.4,1.5,"$y$")
ax1.plot([-0.1,0.1],[1,1],color="black")
ax1.text(-0.4,1,"$1$")

#\varphi_0
ax1.plot([0.5,0.5],[-0.05,0.05],color="black")
ax1.text(0.25,-0.25,"$x_0$")
ax1.plot([2,2],[-0.05,0.05],color="black")
ax1.text(1.75,-0.25,"$x_1$")
ax1.plot([0.5,0.5],[0,1],color="gray",linestyle="dashed")
ax1.plot([0.5,2],[1,0],color="black")
ax1.text(0.5,1.1,r"$\varphi_0$")

ax1.text(3,-0.25,"$\cdots$")

#varphi_1
ax1.plot([4.5,4.5],[-0.05,0.05],color="black")
ax1.text(4.25,-0.25,"$x_{i-1}$")
ax1.plot([5.5,5.5],[-0.05,0.05],color="black")
ax1.text(5.25,-0.25,"$x_{i}$")
ax1.plot([6.5,6.5],[-0.05,0.05],color="black")
ax1.text(6.25,-0.25,"$x_{i+1}$")
ax1.plot([4.5,5.5,6.5],[0,1,0],color="black")
ax1.plot([5.5,5.5],[0,1],color="gray",linestyle="dashed")
ax1.text(5.5,1.1,r"$\varphi_i$")

ax1.text(7.5,-0.25,"$\cdots$")

#varphi_n
ax1.plot([9,9],[-0.05,0.05],color="black")
ax1.text(8.75,-0.25,"$x_{n-1}$")
ax1.plot([10.5,10.5],[-0.05,0.05],color="black")
ax1.text(10.25,-0.25,"$x_n$")
ax1.plot([9,10.5],[0,1],color="black")
ax1.plot([10.5,10.5],[0,1],color="gray",linestyle="dashed")
ax1.text(10.5,1.1,r"$\varphi_n$")



# #ax1.set_xlim((0,1))
# #ax1.set_ylim((0,0.9))
# ax1.grid()
# ax1.legend(loc='upper right',fontsize=8,numpoints=1)
# ax1.set_xlabel("$x$")
# ax1.set_xticks([0,0.2,0.4,0.6,0.8,1.0])
# ax1.set_xticklabels([0.0,0.5,1.0,1.5,2.0,2.5],fontsize=10)
# ax1.set_title("$\Psi(x,2.5)$")

fig.savefig("fig_baselinear.eps",bbox_inches='tight')

