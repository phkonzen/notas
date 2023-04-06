f = @(x) x.^2 - cos(x);
a=0.5;
b=1;

g = @(x,alpha) x - alpha*f(x);
fl = @(x) 2*x + sin(x);
gl = @(x,alpha) 1 - alpha*fl(x);

alpha=0.5

xx=linspace(a,b);
plot(xx,xx,'r--',...
     xx,g(xx,alpha),'b-',...
     xx,abs(gl(xx,alpha)),'k--') 
     
x=(a+b)/2;
for k=1:10
  x=g(x,alpha);
  printf("%1.4E\n",x)
endfor

