#!/bin/python3

import numpy as np
from sympy import *
init_printing()
var('x',real=True)

p1 = plot(-x,(x,-2,0),show=False)
p2 = plot(x**2,(x,0,2),show=False)
p = p1
p.extend(p2)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_ex_funpartes.png')
