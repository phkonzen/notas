import matplotlib.pylab as plt

fig = plt.figure(figsize=(9, 3))
ax = plt.subplot()
ax.set_ylim((2.5,-0.5))
ax.axis("off")

ax.plot([-2,2],[0,0],ls="-",color="black")
ax.plot([-2,2],[1,1],ls="-",color="black")
ax.plot([-2,2],[2,2],ls="-",color="black")

ax.plot([-1,-1],[2.5,-0.5],ls="--",color="gray")
ax.text(-1,-0.1,"$-1$",fontsize=12)
ax.text(-1,2.25,"$-1$",fontsize=12)
ax.text(-1.5,-0.1,"$-$",fontsize=12)
ax.text(0,-0.1,"$+$",fontsize=12)
ax.text(1.5,-0.1,"$+$",fontsize=12)
ax.text(2.1,0,"$x+1$",fontsize=12)
ax.plot([1,1],[2.5,-0.5],ls="--",color="gray")
ax.text(1,-0.1,"$1$",fontsize=12)
ax.text(1,2.25,"$1$",fontsize=12)
ax.text(-1.5,0.9,"$-$",fontsize=12)
ax.text(0,0.9,"$-$",fontsize=12)
ax.text(1.5,0.9,"$+$",fontsize=12)
ax.text(2.1,1.0,"$x-1$",fontsize=12)
ax.text(-1.5,1.9,"$+$",fontsize=12)
ax.text(0,1.9,"$-$",fontsize=12)
ax.text(1.5,1.9,"$+$",fontsize=12)
ax.text(2.1,2.0,"$\\frac{x+1}{x-1}$",fontsize=12)


plt.savefig("fig_cap_lim_exeresol_estsinal.png", bbox="tight")
