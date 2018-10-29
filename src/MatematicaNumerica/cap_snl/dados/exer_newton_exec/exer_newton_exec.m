disp('Newton')

function y = F(x)
  y = zeros(size(x));
  y(1) = x(2)*sin(x(3)) + x(1) - 2;
  y(2) = x(1)*x(2) - sin(x(2)) + 0.2;
  y(3) = x(3)^2 + cos(x(1)*x(2)) - 4.5; 
endfunction

function y = J(x)
  y=zeros(3,3);
  y(1,1) = 1;
  y(1,2) = sin(x(3));
  y(1,3) = x(2)*cos(x(3));
  y(2,1) = x(2);
  y(2,2) = x(1) - cos(x(2));
  y(2,3) = 0;
  y(3,1) = -sin(x(1)*x(2))*x(2);
  y(3,2) = -sin(x(1)*x(2))*x(1);
  y(3,3) = 2*x(3);
endfunction

x = [1 -1 -1]';
disp([1,x',norm(F(x))])
for k=2:7
  x = x - inv(J(x))*F(x);
  disp([k,x',norm(F(x))])
endfor