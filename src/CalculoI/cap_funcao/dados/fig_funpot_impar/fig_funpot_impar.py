import matplotlib.pyplot as plt
from sympy import *
from sympy.abc import *

p = plot(x,(x,-2,2),ylim=(-2,2),show=False,
         line_color="blue")
q = plot(x**3,(x,-2,2),ylim=(-2,2),show=False,
         label='$y=x^3$',line_color="red")
p.extend(q)
q = plot(x**5,(x,-2,2),ylim=(-2,2),show=False,
         label="$y=x^5$",line_color="green")
p.extend(q)
p[0].label="$y=x$"
p[1].label="$y=x^3$"
p[2].label="$y=x^5$"
p.legend = True
p.ylabel="$y$"
p.show()
