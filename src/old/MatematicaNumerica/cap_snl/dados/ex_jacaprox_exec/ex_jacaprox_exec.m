disp('Newton')

function y = F(x)
  y = zeros(size(x));
  y(1) = x(1)*x(2)^2 - x(1)^2*x(2)+6;
  y(2) = x(1) + x(1)^2*x(2)^3-7; 
endfunction

function y = Ja(x)
  h = 1e-7;
  y=zeros(2,2);
  fx1 = F(x + [h 0]');
  fx0 = F(x);
  y(:,1) = (fx1 - fx0)/h;
  fx1 = F(x + [0 h]');
  fx0 = F(x);
  y(:,2) = (fx1 - fx0)/h;
endfunction

x=[-1.5 1.5]';
x0=x;
printf("%d %1.2E %1.2E\n",1,x)
for k=2:5
  x = x - inv(Ja(x))*F(x);
  printf("%d %1.2E %1.2E %1.1E\n",k,x,norm(x-x0))
  x0=x;
endfor