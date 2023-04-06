format short e

f = @(x) x^2*sin(x);
fl = @(x) 2*x*sin(x) + x^2*cos(x);

x=pi/3;

kf = abs(x*fl(x)/f(x))

