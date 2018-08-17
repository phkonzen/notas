f = @(x,y) exp(-x^2)*cos(pi*y/3);
flx = @(x,y) -2*x*exp(-x^2)*cos(pi*y/3);
fly = @(x,y) pi/3*exp(-x^2)*sin(pi*y/3);

x=2;
eax=0,02*abs(x);

y=1.5;
eay=0.3;

eay = abs(flx(x,y))*eax + abs(fly(x,y))*eay;

printf("%1.5E\n",eay)
