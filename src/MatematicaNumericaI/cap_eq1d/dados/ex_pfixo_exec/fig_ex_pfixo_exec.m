f = @(x) sin(x+pi/4).^2-x.^3+pi/4*x.^2+5*pi^2/16*x+3*pi^3/64;
fl = @(x) 2*sin(x+pi/4).*cos(x+pi/4)-3*x.^2+pi/2*x+5*pi^2/16;

g = @(x,alpha) x - alpha*f(x); 
gl = @(x,alpha) 1 - alpha*fl(x);

alpha=-0.1;
xx=linspace(2,3);
plot(xx,xx,'r--',...
     xx,g(xx,alpha),'b-',...
     xx,abs(gl(xx,alpha)),'k--');grid
legend('x=y','g',"g'",'location','northwest')
set(gca,'fontsize',12)