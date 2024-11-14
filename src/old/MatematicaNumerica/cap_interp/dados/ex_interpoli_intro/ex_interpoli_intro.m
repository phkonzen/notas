x = [-1 0 1]';
y = [-1 1 0.5]';
A = [x.^2 x.^1 x.^0]
p = inv(A)*y

xx=linspace(-1.25,1.25);
plot(x,y,'ro',...
     xx,polyval(p,xx),'b-')