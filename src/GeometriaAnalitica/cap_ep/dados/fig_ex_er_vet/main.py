from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import matplotlib.pyplot as plt
#font letter
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=12)

# arrow3d
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

#figure
fig = plt.figure(figsize=(6,6), dpi=300, 
                 linewidth=0.0, facecolor="white")
ax = fig.gca(projection='3d')
ax.axis('on')
ax.set_xlabel('$x$')
ax.set_xticks([-2,-1,0,1,2,3])
ax.set_ylabel('$y$')
ax.set_yticks([-2,-1,0,1,2])
ax.set_zlabel('$z$')
ax.set_zticks([-2,-1,0,1,2,3,4])

plt.plot([-2,3],[-7/3,5/3],[-11/3,14/3],color='black')
plt.plot([-1],[-1],[-2],marker='o',color='black')
ax.text(-1,-1,-2.6,'$A=(-1,-1,-2)$')
plt.plot([2],[1],[3],marker='o',color='black')
ax.text(0.25,1,3,'$B=(2,1,3)$')
ax.add_artist(Arrow3D([-1,2],[-1,1],[-2,3],mutation_scale=20,
                      lw=3,arrowstyle='-|>',color='black'))
ax.text(0,0,0.5,'$\\vec{v}$')
ax.text(-1.5,-2,-2,'$r$')

fig.savefig("fig_ex_er_vet.png", bbox_inches="tight")
