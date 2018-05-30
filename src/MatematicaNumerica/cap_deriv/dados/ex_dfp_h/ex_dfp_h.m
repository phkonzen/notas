f = @(x) sin(x);
Df = @(x,h) (f(x+h)-f(x))/h;
x=pi/3;
h=1e-10;
printf('%1.5e %1.1e\n',Df(x,h),abs(cos(x)-Df(x,h)))
