from sympy import *
init_printing()
var('x')

p = plot((x+1)*(x-1)*(x-2.5),(x,-2,4),show=False)
print(latex(expand((x+1)*(x-1)*(x-2.5))))
p.xlabel = '$x$'
p.ylabel = '$p(x)$'
p.title = '$p(x) = x^{3} - \\frac{5}{2} x^{2} - x + \\frac{5}{2}$'
p.save('fig_poli_impar.png')

p = plot((x+1)*(x-1)**2*(x-2.5),(x,-2,4),ylim=[-6,20],show=False)
print(latex(expand((x+1)*(x-1)**2*(x-2.5))))
p.xlabel = '$x$'
p.ylabel = '$q(x)$'
p.title = '$q(x) = x^{4} - \\frac{7}{2}x^{3} + \\frac{3}{2}x^{2} + \\frac{7}{2}x - \\frac{5}{2}$'
p.save('fig_poli_par.png')
