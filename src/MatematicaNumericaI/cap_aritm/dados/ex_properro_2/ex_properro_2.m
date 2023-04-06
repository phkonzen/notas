format short e

f = @(x,y) x^2*sin(x)*cos(y);
fx = @(x,y) (2*x*sin(x) + x^2*cos(x))*cos(y);
fy = @(x,y) -x^2*sin(x)*sin(y);

x=pi/3;
eax=0.1

y=pi/4;
eay=0.02

eaz = abs(fx(x,y))*eax + abs(fy(x,y))*eay


