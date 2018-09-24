A = [-4 2 -1;...
     -2 5 2;...
     1 -1 -3]
b = [-11 -7 0]';

x = [2 -1 1]';

L = tril(A,-1)
D = diag(diag(A))
U = triu(A,1)

TJ = -inv(D)*(L+U)
cJ = inv(D)*b

TJ*x + cJ