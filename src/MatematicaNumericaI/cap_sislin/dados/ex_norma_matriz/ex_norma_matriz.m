A = [1 -1 2; ...
     -2 pi 4; ...
     7 -5 sqrt(2)]

autoval = eig(A'*A)
normal2 = sqrt(max(abs(autoval)))
norm(A)