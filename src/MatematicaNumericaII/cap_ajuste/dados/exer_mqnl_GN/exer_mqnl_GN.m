#pontos
global x = [-0.5 0.5 1.3 2.1 2.7 3.1]';
y = [0.1 1.2 2.7 0.9 0.2 0.1]';

#fun. objetivo
f = @(x,c) c(1)*exp(c(2)*(x-c(3)).^2);

#residuo
r = @(c) y - f(x,c);

#jacobiana
function A = JR(c)
  global x
  A = zeros(6,3);
  A(:,1) = -exp(c(2)*(x-c(3)).^2);
  A(:,2) = -c(1)*(x-c(3)).^2 .* exp(c(2)*(x-c(3)).^2);
  A(:,3) = 2*c(1)*c(2)*(x-c(3)) .* exp(c(2)*(x-c(3)).^2);
endfunction

#aprox. inicial
c = [2.1 -1 1.3]';
%c = [1 -1 -1]';

#iteracoes de Gauss-Newton
k=0;
do
  k+=1;
  delta = - JR(c)\r(c);
  c = c + delta;
  printf("%d %1.1e %1.1e %1.1e %1.1e\n", k,norm(delta),c')
until ((k>10) | (norm(delta)<1e-4))

printf('%1.5e\n',c)

xx=linspace(-0.6,3.2);
plot(x,y,'ro',...
     xx,f(xx,c),'b-');grid

