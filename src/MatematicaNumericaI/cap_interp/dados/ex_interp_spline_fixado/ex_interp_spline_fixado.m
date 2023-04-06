x = [0 pi/3 pi/6 pi/2]';
y = sin(x);

s = spline(x,[1;y;0])

xx=linspace(0,pi/2);
plot(x,y,'ro',...
     xx,sin(xx),'r-',...
     xx,ppval(s,xx),'b-');grid
legend("pts","f","spline","location","northwest")
