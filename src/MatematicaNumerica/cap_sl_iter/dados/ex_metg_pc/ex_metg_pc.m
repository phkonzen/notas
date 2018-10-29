A = [2 -1 0 0;...
     -1 2 -1 0;...
     0 -1 2 -1;...
     0 0 -1 2]
b = [-3 2 2 -3]'

alpha=5e-1;
x = [0 0 0 0]'
r = A*x - b;
disp([x',norm(r)])

for k=2:11
  x = x - alpha*r;
  r = A*x - b;
  disp([x',norm(r)])
endfor