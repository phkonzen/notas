f = @(x) sin(x+pi/4).^2-x.^3+pi/4*x.^2+5*pi^2/16*x+3*pi^3/64;
alpha=-0.05;
g = @(x) x - alpha*f(x); 


x0=2.6;
printf("%d %1.4E\n",1,x0)
for k=2:4
  x1=g(x0);
  x2=g(x1);
  x=x0-(x1-x0)^2/(x2-2*x1+x0);
  printf("%d %1.4E %1.1E\n",...
          k,x,abs(x-x0))
  x0=x;
endfor