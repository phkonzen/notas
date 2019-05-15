import matplotlib.pyplot as plt
#font letter
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=12)

#figure
fig = plt.figure(figsize=(4,2), dpi=300, 
                 linewidth=0.0, facecolor="white")
ax = plt.subplot(1,1,1)
ax.axis('off')

plt.plot([0,1],[0.1,0.9],color='black')
plt.text(0.075,0.2,'$r$')
plt.plot([0.3],[0.34],marker='o',color='black')
plt.text(0.3,0.25,'$A$')
plt.plot([0.7],[0.66],marker='o',color='black')
plt.text(0.625,0.7,'$P$')
plt.arrow(0.6,0.25,0.2,0.8*0.2,head_width=0.02,facecolor='black')
plt.text(0.7,0.25,'$\\vec{v}$')


fig.savefig("fig_er_vet.pdf", bbox_inches="tight")
