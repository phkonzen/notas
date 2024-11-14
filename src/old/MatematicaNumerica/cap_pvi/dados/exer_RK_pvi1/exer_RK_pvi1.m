f = @(t,y) 2 - exp(-y^2+1);

h=1e-1;
n=fix(1/h+1);
t=zeros(n,1);
y=zeros(n,1);

t(1)=1;
y(1)=-1;

#pto. medio
for i=1:n-1
  t(i+1) = t(i)+h;
  y(i+1)=y(i)+h*f(t(i)+h/2,y(i)+h/2*f(t(i),y(i)));
endfor
printf("%1.5E %1.5E\n",t(n),y(n))

#Euler melhorado
for i=1:n-1
  t(i+1) = t(i)+h;
  y(i+1)=y(i)+h/2*(f(t(i),y(i))+f(t(i)+h,y(i)+h*f(t(i),y(i))));
endfor
printf("%1.5E %1.5E\n",t(n),y(n))

#R-K-4
for i=1:n-1
  t(i+1) = t(i)+h;
  k1 = h*f(t(i),y(i));
  k2 = h*f(t(i)+h/2,y(i)+k1/2);
  k3 = h*f(t(i)+h/2,y(i)+k2/2);
  k4 = h*f(t(i)+h,y(i)+k3);
  y(i+1)=y(i)+(k1+2*k2+2*k3+k4)/6;
endfor
printf("%1.5E %1.5E\n",t(n),y(n))
