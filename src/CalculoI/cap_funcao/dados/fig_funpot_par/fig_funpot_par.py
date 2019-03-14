from sympy import *
from sympy.abc import *

p = plot(x**2,(x,-2,2),ylim=(-2,2),show=False,
         line_color="blue")
q = plot(x**4,(x,-2,2),ylim=(-2,2),show=False,
         line_color="red")
p.extend(q)
q = plot(x**6,(x,-2,2),ylim=(-2,2),show=False,
         line_color="green")
p.extend(q)
p[0].label="$y=x^2$"
p[1].label="$y=x^4$"
p[2].label="$y=x^6$"
p.legend = True
p.ylabel="$y$"
p.save('fig_funpot_par.png')
