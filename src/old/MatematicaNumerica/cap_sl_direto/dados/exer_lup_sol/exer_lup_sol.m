A = [-1 2 -2;...
     3 -4 1;...
     -4 -5 3]
%x = [-3 -1 1]';
%A*x
b = [-1 -4 20]'

#decomposicao LUP
n=size(A,1);
P=eye(n,n);
L=eye(n,n);
U=A;
for i=1:n-1
  [aux,j]=max(A(i:n,i));
  j+=i-1
  aux=P(i,:);
  P(i,:)=P(j,:);
  P(j,:)=aux;
  aux=L(i,1:i-1);
  L(i,1:i-1)=L(j,1:i-1);
  L(j,1:i-1)=aux;
  aux=U(i,:);
  U(i,:)=U(j,:);
  U(j,:)=aux;
  L(i+1:n,i)=U(i+1:n,i)/U(i,i);
  U(i+1:n,:)-=L(i+1:n,i)*U(i,:);
endfor
P
L
U
     
#Ly = Pb
b = P*b;
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



