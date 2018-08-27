f = @(x) sin(x+pi/4).^2-x.^3+pi/4*x.^2+5*pi^2/16*x+3*pi^3/64;
fl = @(x) 2*sin(x+pi/4).*cos(x+pi/4)-3*x.^2+pi/2*x+5*pi^2/16;
fll = @(x) 2*cos(x+pi/4)^2-2*sin(x+pi/4)^2-6*x+pi/2;

xstar = -pi/4;

x = -0.5;
printf("%d %1.4E %1.1E\n",...
          1,x,abs(x-xstar))
for k=2:5
  x = x - fl(x)/fll(x);
  printf("%d %1.4E %1.1E\n",...
          k,x,abs(x-xstar))
endfor