f = @(x) sin(x);
Df = @(x,h) (f(x+h)-f(x-h))/(2*h);
x=pi/3;
h=1e-5;
printf('%1.5E %1.1E\n',Df(x,h),abs(cos(x)-Df(x,h)))
