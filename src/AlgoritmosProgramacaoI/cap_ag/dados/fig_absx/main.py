import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
     "font.size": 12,
     "figure.dpi": 300
     })


# figure
fig = plt.figure()
# axis
ax = fig.add_subplot()
# plot
ax.plot([-0.5, 0, 1],
        [0.5, 0, 1])
# display
plt.savefig('fig.png', dpi=300, bbox_inches='tight')
plt.show()
