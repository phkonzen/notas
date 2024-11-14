#params
n=81;
h=1/(n-1);

tf=1.0;
ht=0.5*h^2;
nt=round(tf/ht)+1;

#fonte
function y = f(x)
  y = zeros(size(x));
  for i=1:length(x)
    if (x(i)<=0.5)
      y(i)=1;
    else
      y(i)=0;
    endif
  endfor
endfunction

#malha
t=[0:ht:(nt-1)*ht]'; 
x=[0:h:(n-1)*h]';

#matriz MDF
A = sparse(n-2,n-2);
A(1,1)=-2/h^2;
A(1,2)=1/h^2;
for i=2:n-3
  A(i,i-1)=1/h^2;
  A(i,i)=-2/h^2;
  A(i,i+1)=1/h^2;
endfor
A(n-2,n-3)=1/h^2;
A(n-2,n-2)=-2/h^2;

#c.i.
u=zeros(n,1);
u(1)=1;

#iter. de Euler
for k=1:nt-1
  u(2:n-1)=u(2:n-1)+ht*A*u(2:n-1);
  #+fonte
  u(2:n-1)+=ht*f(x(2:n-1));
  #+cc
  u(2)+=ht*1/h^2;
endfor

#visu
plot(x,u,'b.-');grid
xlabel('x');
ylabel('u');
printf("%d %1.5E %1.5E %1.2E\n",t(nt),h,x((n-1)/2+1),u((n-1)/2+1))

