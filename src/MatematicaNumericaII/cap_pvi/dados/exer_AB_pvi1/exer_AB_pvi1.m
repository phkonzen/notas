f = @(t,y) 2-exp(-y^2+1);

h=1e-1;
n=round(1/h+1);
t=zeros(n,1);
y=zeros(n,1);

#c.i.
t(1)=1;
y(1)=-1;

#AB-2
#inicial. Euler
t(2)=t(1)+h;
for i=1:1
  y(i+1)=y(i)+h*f(t(i),y(i));
endfor

#iteracoes
for i=2:n-1
  t(i+1) = t(i)+h;
  y(i+1)=y(i) + ...
        h/2*(3*f(t(i),y(i))-f(t(i-1),y(i-1)));
endfor

printf("%f %1.5E\n",t(n),y(n))

#AB-3
#inicial. Euler
t(2)=t(1)+h;
for i=1:2
  y(i+1)=y(i)+h*f(t(i),y(i));
endfor

#iteracoes
for i=3:n-1
  t(i+1) = t(i)+h;
  y(i+1)=y(i) + ...
        h/12*(23*f(t(i),y(i)) ...
        -16*f(t(i-1),y(i-1)) ...
        +5*f(t(i-2),y(i-2)));
endfor

printf("%f %1.5E\n",t(n),y(n))

#AB-4
#inicial. Euler
t(2)=t(1)+h;
for i=1:3
  y(i+1)=y(i)+h*f(t(i),y(i));
endfor

#iteracoes
for i=4:n-1
  t(i+1) = t(i)+h;
  y(i+1)=y(i) + ...
        h/24*(55*f(t(i),y(i)) ...
        -59*f(t(i-1),y(i-1)) ...
        +37*f(t(i-2),y(i-2)) ...
        -9*f(t(i-3),y(i-3)));
endfor

printf("%f %1.5E\n",t(n),y(n))
