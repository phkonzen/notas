A = [-4 2 -1;...
     -2 5 2;...
     1 -1 -3];
b = [-11 -7 0]';
n=size(A,1);

x = [0 0 0]';
disp([x',norm(A*x-b)])
for k=2:5
  for i=1:n
    x(i) = (b(i) - A(i,[1:i-1,i+1:n])*x([1:i-1,i+1:n]))/A(i,i);
  endfor
  disp([x',norm(A*x-b)])
endfor
