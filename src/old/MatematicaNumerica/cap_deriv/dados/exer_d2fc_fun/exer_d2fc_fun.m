f = @(x) (sin(x+2) - exp(-x.^2))./(x.^2 + log(x+2))+x;
x=2.5;
h=1e-4;
d2f = (f(x+h) - 2*f(x) + f(x-h))/h^2;

printf("%1.5E\n",d2f)