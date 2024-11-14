f = @(x) sin(x) + x^2;
Df = @(x,h) (f(x+h)-f(x-h))/(2*h);
DDf = @(x,h) (Df(x+h,h)-Df(x-h,h))/(2*h);
D2f = @(x,h) (f(x+h) - 2*f(x) + f(x-h))/(h^2);
x=pi/6;
h=1e-10;

printf('%1.5E %1.1E %1.5E %1.1E\n',...
  DDf(x,h),abs(1.5-DDf(x,h)),...
  D2f(x,h),abs(1.5-D2f(x,h)))
