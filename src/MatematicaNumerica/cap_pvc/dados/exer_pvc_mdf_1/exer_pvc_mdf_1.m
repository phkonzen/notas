#param
n = 1001;
h = 2/(n-1);

#fonte
function y = f(x)
  if (x <= 0)
    y=1;
  else
    y=0;
  endif
endfunction

#nodos
x = linspace(-1,1,n)';

#sist. MDF
A = zeros(n,n);
b = zeros(n,1);

A(1,1) = 1;
b(1)=0;
for i=2:n-1
  A(i,i-1)=-1/h^2+1/(2*h);
  A(i,i)=2/h^2;
  A(i,i+1)=-1/h^2-1/(2*h);
  b(i)=f(x(i));
endfor
A(n,n)=1;
A(n,n-1)=-1;
b(n)=0;

#sol MDF
u = A\b;

#erro na norma L2
k=(n-1)/2+1;
printf("%d %1.5E\n", x(k),u(k))