f = @(x) sin(x+pi/4).^2-x.^3+pi/4*x.^2+5*pi^2/16*x+3*pi^3/64;

xstar = 3*pi/4;

phi = (1+sqrt(5))/2

x1 = 2.6;
x2 = 2.5;
for k=3:10
  x = x2 - f(x2)*(x2-x1)/(f(x2)-f(x1));
  printf("%d %1.4E %1.1E\n",...
          k,x,abs(x-xstar))
  x1=x2;
  x2=x;
endfor