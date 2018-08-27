f = @(x) x.^3 .* sin(x) - cos(x);
fl = @(x) 3*x.^2 .* sin(x) + x.^3 * cos(x) + sin(x);

x=0.75
x0=x;
printf("%d %1.4E\n",1,x)
for k=1:5
  x=x0-f(x0)/fl(x0);
  printf("%d %1.4E %1.1E\n",1,x,abs(x-x0))
  x0=x;
endfor