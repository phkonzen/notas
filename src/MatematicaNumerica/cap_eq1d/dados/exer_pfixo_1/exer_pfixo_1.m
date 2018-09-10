f = @(x) x - cos(x);
fl = @(x) 1 + sin(x);

alpha=0.6
g = @(x) x - alpha*f(x);
gl = @(x) 1 - alpha*fl(x);

a=0.5;
b=1;

xx=linspace(a,b);
plot(xx,xx,'r--',...
     xx,g(xx),'b-',...
     xx,abs(gl(xx)),'k--');grid

x=(a+b)/2;
for k=1:3
  x=g(x)
endfor
printf("%1.4E\n",x)