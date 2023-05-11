pkg load symbolic;
syms x;

f = @(x) (-x.^2+1.154*x-0.332929).*cos(x) + x.^2 - 1.154*x + 0.332929;
fl = function_handle(diff(f(x),x));
fll = function_handle(diff(f(x),x,2));

x=0.6
x0=x;
printf("%d %1.3E\n",1,x)
for k=1:4
  x=x0-fl(x0)/fll(x0);
  printf("%d %1.4E %1.1E\n",1,x,abs(x-x0))
  x0=x;
endfor