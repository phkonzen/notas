f = @(t,y) 2 - exp(-y^2+1);

h=0.1;
n=11;
t=zeros(n,1);
y=zeros(n,1);

t(1)=1;
y(1)=-1;

for i=1:n-1
  t(i+1) = t(i)+h;
  y(i+1)=y(i)+h*f(t(i),y(i));
endfor

printf("%1.5E %1.5E\n",t(n),y(n))