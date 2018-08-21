f = @(x) (2*x.^3-1.4*x.^2-0.98*x+0.686).*exp(-x.^2)-...
         (x.^3-0.7*x.^2-0.49*x+0.343).*exp(-x.^4);
xx=linspace(-2,2);
plot(xx,f(xx));grid
hold onx
xx=[-0.7 0.7];
plot(xx,f(xx),'ro');
legend("f","zeros","location","northwest")
set(gca,"fontsize",12)
hold off