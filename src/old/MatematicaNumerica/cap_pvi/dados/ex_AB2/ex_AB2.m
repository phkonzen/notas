f = @(t,y) y+sin(t);

h=1e-1;
n=round(1/h+1);
t=zeros(n,1);
y=zeros(n,1);

#c.i.
t(1)=0;
y(1)=0.5;

#inicializacao
t(2)=t(1)+h;
y(2)=y(1)+h*f(t(1)+h/2,y(1)+h/2*f(t(1),y(1)));

#iteracoes
for i=2:n-1
  t(i+1) = t(i)+h;
  y(i+1)=y(i) + ...
        h/2*(3*f(t(i),y(i))-f(t(i-1),y(i-1)));
endfor

ya = @(t) exp(t)-sin(t)/2-cos(t)/2;
printf("%f %1.5E %1.1E\n",t(n),y(n),abs(y(n)-ya(1)))
