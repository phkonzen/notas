pkg load symbolic
syms x
f = (2*x.^3-1.4*x.^2-0.98*x+0.686).*exp(-x.^2)-...
         (x.^3-0.7*x.^2-0.49*x+0.343).*exp(-x.^4);
         
fl = matlabFunction(diff(f))

xx=linspace(0.5,1);
plot(xx,fl(xx),'b-',...
     0.7,fl(0.7),'ro');grid
legend("fl","zero","location","northwest")
set(gca,"fontsize",12)