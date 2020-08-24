from sympy import *
t = symbols('t')
y0 = 0.5
p = plot(y0/(y0+(1-y0)*exp(-0.1*t)), (t,0,50), 
         line_color="blue", show="False")
y0 = 1
q = plot(y0/(y0+(1-y0)*exp(-0.1*t)), (t,0,50), 
         line_color="black", show="False")
p.extend(q)
y0 = 1.5
q = plot(y0/(y0+(1-y0)*exp(-0.1*t)), (t,0,50), 
         line_color="red", show="False")
p.extend(q)
p.ylabel="$y(t)$"
p.show()
    

#y = symbols('y', cls=Function)
#x,C1 = symbols('x,C1')
#edo = Eq(diff(y(x),x),x**2/y(x))
#sg = dsolve(edo, y(x), simplify=False)
#sg
#
#var('y')
#sg = sg.subs(y(x),y)
#p = plot_implicit(sg.subs(C1,-1), (x,-4,4), \
#         (y,-4,4), line_color="blue", show=False)
#q = plot_implicit(sg.subs(C1,0), (x,-4,4), \
#         (y,-4,4), line_color="red", show=False)
#p.extend(q)
#q = plot_implicit(sg.subs(C1,1), (x,-4,4), \
#         (y,-4,4), line_color="green", show=False)
#p.extend(q)
#q = plot_implicit(sg.subs(C1,2), (x,-4,4), \
#         (y,-4,4), line_color="black", show=False)
#p.extend(q)
#p.show()
