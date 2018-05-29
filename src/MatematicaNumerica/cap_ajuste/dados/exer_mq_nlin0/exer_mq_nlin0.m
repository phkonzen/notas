#pontos
x = [-0.5 0.5 1.3 2.1 2.7 3.1]';
y = [0.1 1.2 2.7 0.9 0.2 0.1]';

#resol. as eqs. normais
A = [x.^2 x ones(6,1)];
d = inv(A'*A)*A'*log(y);

c = zeros(3,1);
c(2) = d(1);
c(3) = d(2)/(-2*c(2));
c(1) = exp(d(3) - c(2)*c(3)^2);

printf('%1.5e\n',c)

#fun. ajustada
f = @(x) c(1)*exp(c(2)*(x-c(3)).^2);

#esboco da fun. ajustada
xx = linspace(-0.6,3.2);
plot(x,y,'ro',...
     xx,f(xx),'b-');grid
     