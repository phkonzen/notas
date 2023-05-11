pkg load symbolic
syms x
f = @(x) sin(x+pi/4).^2-x.^3+pi*x.^2/4+5*pi^2*x/16+3*pi^3/64;
fl = function_handle(diff(f(x)));

xx=linspace(-2,3);
plot(xx,f(xx),'b-',...
     xx,fl(xx),'r-',...
     -pi/4,fl(-pi/4),'ro');grid
legend("f","f'","zero","location","northeast")
set(gca,"fontsize",12)