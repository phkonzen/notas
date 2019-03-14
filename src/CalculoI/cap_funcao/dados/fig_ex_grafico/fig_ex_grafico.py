from sympy import *
var('x')

p = plot(x**2,(x,-2,2),label="$f(x)=x^2$",show=False);
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_ex_grafico_x2.png')

p = plot(1/x,(x,-2,2),ylim=(-6,6),label="$g(x)=1/x$",show=False);
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_ex_grafico_1x.png')

p = plot(sqrt(1-x**2),(x,-1,1),
         label="$h(x)=\sqrt{1-x^2}$",show=False);
p.xlabel = '$x$'
p.ylabel = '$y$'
p.save('fig_ex_grafico_s1x2.png')
