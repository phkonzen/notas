A = [-4 2 -1;...
     -2 5 2;...
     1 -1 -3];
b = [-11 -7 0]';

L = tril(A,-1);
D = diag(diag(A));
U = triu(A,1);

TJ = -inv(D)*(L+U);
rhoTJ = max(abs(eig(TJ)))

TG = -inv(L+D)*U;
rhoTG = max(abs(eig(TG)))