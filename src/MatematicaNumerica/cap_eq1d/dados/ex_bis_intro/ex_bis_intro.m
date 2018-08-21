f = @(x) sin(x+pi/4).^2-x.^3+pi*x.^2/4+5*pi^2*x/16+3*pi^3/64;
xx=linspace(-2,3);
plot(xx,f(xx));grid
