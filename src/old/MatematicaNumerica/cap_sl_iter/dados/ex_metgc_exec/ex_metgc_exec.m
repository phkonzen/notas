A = [2 -1 0 0;...
     -1 2 -1 0;...
     0 -1 2 -1;...
     0 0 -1 2]
x = [-1 1 1 -1]';
b = [-3 2 2 -3]'

x = [0 0 0 0]'
r = A*x - b;
d = r;
disp([x',norm(r)])

for k=2:3
  alpha = r'*d/(d'*A*d);
  x = x - alpha*d;
  r = A*x - b;
  disp([x',norm(r)])
  beta=r'*A*d/(d'*A*d);
  d=-r+beta*d;
endfor




