A = [-1 2 -2;...
     3 -4 1;...
     1 -5 3]
b = [6 -11 -10]'

#decomposicao LU
L = [1 0 0; ...\\
     -3 1 0; ...
     -1 -1.5 1]
U = [-1 2 -2;...
     0 2 -5;...
     0 0 -6.5]
     
#Ly = b
n=length(b);
y=zeros(n,1);
for i=1:n
  y(i) = (b(i)-L(i,1:i-1)*y(1:i-1));
endfor
y

#Ux = y
x=zeros(n,1);
for i=n:-1:1
  x(i) = (y(i) - U(i,i+1:n)*x(i+1:n))/U(i,i);
endfor
x



