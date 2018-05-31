f = @(x) (sin(x+2) - exp(-x^2))/(x^2+log(x+2))+x;
x=2.5;
h=1e-2;
dfp = (f(x+h)-f(x))/h
dfr = (f(x)-f(x-h))/h
dfc = (f(x+h)-f(x-h))/(2*h)

printf("%1.5E\n",dfp,dfr,dfc)