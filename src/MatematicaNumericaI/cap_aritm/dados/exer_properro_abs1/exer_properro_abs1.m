f = @(x) exp(-x^2)*cos(pi*x/3);
fl = @(x) -2*x*exp(-x^2)*cos(pi*x/3) - ...
          pi/3*exp(-x^2)*sin(pi*x/3);
x=2;
eax=0.1;

eay = abs(fl(x))*eax;

printf("%1.6E\n",eay)
