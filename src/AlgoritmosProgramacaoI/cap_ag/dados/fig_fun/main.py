import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
     "font.size": 12,
     "figure.dpi": 300
     })

# figure
fig = plt.figure(dpi=300)
# axis
ax = fig.add_subplot()
# -2 <= x < -0.5
x = np.linspace(-2, -0.5)
ax.plot(x, -(x+1)**2-2)
# -0.5 <= x < 1
x = np.linspace(-0.5, 1)
ax.plot(x, np.fabs(x))
# 1 <= x < 3
x = np.linspace(1, 3)
ax.plot(x, (x-2)**3+2)
# display
plt.savefig('fig.png', bbox_inches='tight')
plt.show()
