f = @(x) (sin(x+2) - exp(-x^2))/(x^2+log(x+2))+x;
x = 2.5;
h = 0.1;
df = (f(x-2*h)-8*f(x-h)+8*f(x+h)-f(x+2*h))/(12*h);
printf("%1.5E\n",df)