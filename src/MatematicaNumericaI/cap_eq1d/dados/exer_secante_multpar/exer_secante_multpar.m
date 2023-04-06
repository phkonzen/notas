pkg load symbolic;
syms x;

f = @(x) (-x.^2+1.154*x-0.332929).*cos(x) + x.^2 - 1.154*x + 0.332929;
fl = function_handle(diff(f(x),x));

x1=0.59;
x2=0.58;
for k=3:5
  x=x2-fl(x2)*(x2-x1)/(fl(x2)-fl(x1));
  printf("%d %1.4E\n",k,x)
  x1=x2;
  x2=x;
endfor