disp('Newton')

function y = F(x)
  y = zeros(size(x));
  y(1) = x(1)*x(2)^2 - x(1)^2*x(2)+6;
  y(2) = x(1) + x(1)^2*x(2)^3-7; 
endfunction

function y = J(x)
  y=zeros(2,2);
  y(1,1) = x(2)^2-2*x(1)*x(2);
  y(1,2) = 2*x(1)*x(2)-x(1)^2;
  y(2,1) = 1+2*x(1)*x(2)^3;
  y(2,2) = 3*x(1)^2*x(2)^2;
endfunction

xx1 = linspace(-2,2.25);
xx2 = xx1;
zz = zeros(length(xx1),length(xx2));
for i = 1:length(xx1)
  for j = 1:length(xx2)
    zz(j,i) = norm(F([xx1(i),xx2(j)]));
  endfor
endfor

meshc(xx1,xx2,zz)
xlabel("x1")
ylabel("x2")

xstar = [-1 2]';
x=[-1.5 1.5]';
printf("%d %1.2E %1.2E %1.1E\n",1,x,norm(x-xstar))
for k=2:5
  x = x - inv(J(x))*F(x);
  printf("%d %1.2E %1.2E %1.1E\n",k,x,norm(x-xstar))
endfor