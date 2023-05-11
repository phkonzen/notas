f = @(x) x.^3 .* sin(x) - cos(x);

x1=0.8;
x2=0.9;
for k=3:6
  x=x2-f(x2)*(x2-x1)/(f(x2)-f(x1));
  printf("%d %1.4E\n",k,x)
  x1=x2;
  x2=x;
endfor