f = @(x) sin(x);
x = [0 pi/2 pi]';
y = f(x);

paux = poly([x(2) x(3)]);
L1 = paux/polyval(paux,x(1))

paux = poly([x(1) x(3)]);
L2 = paux/polyval(paux,x(2))

paux = poly([x(1) x(2)]);
L3 = paux/polyval(paux,x(3))

p = y(1)*L1 + y(2)*L2 + y(3)*L3

xx=linspace(0,pi);
plot(x,y,'ro',...
     xx,f(xx),'r-',...
     xx,polyval(p,xx),'b-')
legend("pts","f","poli")