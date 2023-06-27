import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 14
     })

fig, ax = plt.subplots()
ax.grid()
ax.set_yticks([-1,0,1])
ax.set_ylabel('$y = \mathrm{sign}(p)$')
ax.set_xlabel('p')
ax.plot([-2.1,0], [-1,-1], color='blue')
ax.plot([0,2.1], [1,1], color='blue')
ax.plot([0],[-1], marker='o', color='blue', mfc = 'white')
ax.plot([0],[0], marker='o', color='blue')
ax.plot([0],[1], marker='o', color='blue', mfc = 'white')

plt.savefig('fig.pdf', bbox_inches='tight')
