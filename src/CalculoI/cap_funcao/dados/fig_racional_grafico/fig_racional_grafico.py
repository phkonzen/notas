from sympy import *
init_printing()
var('x')

r = (x+1)*(x-2)/((x**2+1)*(x-1))
print(latex(expand(r)))
p = plot(r,(x,-5,5),ylim=[-5,5],show=False)
p.xlabel = '$x$'
p.ylabel = '$y$'
p.title = '$f(x) = \\frac{x^{2} - x - 2}{x^{3} - x^{2} + x - 1}$'
p.save('fig_racional_grafico.png')
