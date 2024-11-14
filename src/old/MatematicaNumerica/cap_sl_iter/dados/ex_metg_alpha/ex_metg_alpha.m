A = [2 -1 0 0;...
     -1 2 -1 0;...
     0 -1 2 -1;...
     0 0 -1 2]
x = [-1 1 1 -1]';
b = [-3 2 2 -3]'

x = [0 0 0 0]'
r = A*x - b;
disp([x',norm(r)])

for k=2:5
  alpha = r'*r/(r'*A*r);
  x = x - alpha*r;
  r = A*x - b;
  disp([x',norm(r)])
endfor




