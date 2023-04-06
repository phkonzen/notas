#params
n=161;
h=1/(n-1);

#fonte
function y = f(x,y)
  if ((x<=0.5) && (y<=0.5))
    y=1;
  else
    y=0;
  endif
endfunction

#malha
x = linspace(0,1,n);
y = linspace(0,1,n);

#sistema MDF
#A = zeros(n*n,n*n);
A = sparse(n*n,n*n);
b = zeros(n*n,1);

#cc x=0 e x=1
for i=[1,n]
  for j=1:n
    k = j + (i-1)*n;
    A(k,k)=1;
    b(k) = 0;
  endfor
endfor

#cc y=0
for i=2:n-1
  k = 1 + (i-1)*n;
  A(k,k)=1;
  A(k,k+1)=-1;
  b(k)=0;
endfor

#cc y=1
for i=1:n
  k = n + (i-1)*n;
  A(k,k)=1;
  b(k) = 0;
endfor

#nodos internos
for i=2:n-1
  for j=2:n-1
    k = j + (i-1)*n;
    A(k,k-n) = -1/h^2;
    A(k,k-1) = -1/h^2;
    A(k,k) = 4/h^2;
    A(k,k+1) = -1/h^2;
    A(k,k+n) = -1/h^2;
    
    b(k) = f(x(i),y(j));
  endfor
endfor

u = A\b;

#visu
z = zeros(n,n);
for i=1:n
  for j=1:n
    k = i + (j-1)*n;
    z(i,j) = u(k);
  endfor
endfor
colormap("cool")
mesh(x,y,z)
xlabel('x')
ylabel('y')
zlabel('u')

#u = u(0.5,0.5)
i=round(n/2);
j=round(n/2);
printf("%1.5E %1.5E %1.5E\n",x(i),y(j),u(j+(i-1)*n))