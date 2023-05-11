pkg load symbolic;
syms x;
f = @(x) x.^3 .* sin(x)-cos(x);
fl = function_handle(diff(f(x)));

alpha=0.1;
g = @(x) x - alpha*f(x); 
gl = @(x) 1 - alpha*fl(x);

xx=linspace(0.5,1);
plot(xx,xx,'r--',...
     xx,g(xx),'b-',...
     xx,gl(xx),'k--'); 


x0=0.9;
printf("%d %1.5E\n",1,x0)
for k=2:4
  x1=g(x0);
  x2=g(x1);
  x=x0-(x1-x0)^2/(x2-2*x1+x0);
  printf("%d %1.5E\n",k,x)
  x0=x;
endfor