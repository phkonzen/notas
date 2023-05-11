f = @(x) (x-1).*exp(-x.^2);
fl = @(x) (1-2*x.*(x-1)).*exp(-x.^2);
r1 = @(x) fl(0.5)*(x-0.5)+f(0.5);
r2 = @(x) fl(1.5)*(x-1.5)+f(1.5);

xx = linspace(0.25,3);
xx1 = linspace(0.25,1);
xx2 = linspace(1.25,3);
plot(xx,f(xx),'b-',"linewidth",1,...
     0.5,f(0.5),'ro',...
     1.5,f(1.5),'ro',...
     xx1,r1(xx1),'r-',...
     xx2,r2(xx2),'r-',...
     1,f(1),'r.');grid
set(gca,"fontsize",12)
pause()

