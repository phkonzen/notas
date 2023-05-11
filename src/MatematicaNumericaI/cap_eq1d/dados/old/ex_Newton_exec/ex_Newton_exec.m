f = @(x) sin(x+pi/4).^2-x.^3+pi/4*x.^2+5*pi^2/16*x+3*pi^3/64;
fl = @(x) 2*sin(x+pi/4).*cos(x+pi/4)-3*x.^2+pi/2*x+5*pi^2/16;

x = 2.6
x0 = x;
for k=2:5
  x = x0 - f(x0)/fl(x0);
  printf("%d %1.4E %1.1E\n",...
          k,x,abs(x-x0))
  x0=x;
endfor