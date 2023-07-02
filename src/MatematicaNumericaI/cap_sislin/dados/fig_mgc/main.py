import numpy as np
import numpy.linalg as npla
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 14
     })


A = np.array([[3., 0.4],
              [0.4, 2.]])
xs = np.array([1., 1.])
b = A@xs

fig = plt.figure(dpi=300)
ax = fig.add_subplot()

xx = np.linspace(0., 2.)
yy = np.linspace(0., 2.)
X,Y = np.meshgrid(xx, yy)
Z = np.empty_like(X)
for i,yj in enumerate(yy):
    for j,xi in enumerate(xx):
        x = np.array([xi,yj])
        Z[i,j] = npla.norm(b - A@x)

x0 = np.array([1.75, 1.75])
r = b - A@x0
d = r.copy()
p = [npla.norm(r)]

for i in range(3):
    rdr = np.dot(r,r)
    Ad = A@d
    alpha = rdr/np.dot(d,Ad)
    x = x0 + alpha*d
    ax.plot([x0[0], x[0]], [x0[1], x[1]], ls='--', marker='o', color='blue')
    
    r = r - alpha*Ad
    p.append(npla.norm(r))
    
    beta = np.dot(r,r)/rdr
    d = r + beta*d
    x0 = x.copy()

ax.plot([xs[0]], [xs[1]], marker='o', color='red')

levels = np.linspace(p[1] , p[0], 6)
ax.contour(X, Y, Z, levels=levels, colors='black')

        
ax.set_aspect('equal')
ax.set_xticklabels([])
ax.set_xlabel('$x_1$')
ax.set_yticklabels([])
ax.set_ylabel('$x_2$')
ax.grid()

fig.savefig('fig.pdf')
fig.savefig('fig.png')
