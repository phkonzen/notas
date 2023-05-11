f = @(x) sin(x+pi/4).^2-x.^3+pi/4*x.^2+5*pi^2/16*x+3*pi^3/64;

alpha=-0.05;
g = @(x) x - alpha*f(x); 

x=2.6
printf("%d %1.4E\n",1,x)
x1=g(x);
printf("%d %1.4E\n",2,x1)
for k=3:8
  x2=g(x1);
  d=x-(x1-x)^2/(x2-2*x1+x);
  printf("%d %1.4E %1.4E\n",k,x2,d)

  x=x1;
  x1=x2;
endfor