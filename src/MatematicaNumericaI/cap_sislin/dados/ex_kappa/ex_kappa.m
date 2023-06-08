A = [1 -1 2;...
     -2 pi 4; ...
     7 -5 sqrt(2)]

num_cond = norm(A)*norm(inv(A))
cond(A)

B = [1 0 0; ...
     0 0 -2; ...
     1e5 1e-4 1e5]
cond(B)

%A = diag([1 1e-8 -2])
%x=[-1 1 2]';
%E = [A A*x]
%cond(A)
%
%aux=E(2,:);
%E(2,:)=E(3,:);
%E(3,:)=aux
%
%E(3,:)+=10*E(1,:)
%E(3,:)-=5*E(2,:)
%
%E(3,:)*=1e4
%
%
%cond(E(:,1:3))
%rref(E)
%
%A = [1 0 0; ...
%     0 0 -2; ...
%     1e5 1e-4 1e5]
%cond(A)