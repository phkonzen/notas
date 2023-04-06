f = @(x) (sin(x+2)-e^(-x^2))/(x^2+log(x+2));
a=-1;
b=0;

%pto. medio
h=(b-a);
Ipm = h*f((a+b)/2);
printf("%1.5E\n",Ipm)

%trapezio
h=(b-a);
Itr = h/2*(f(a)+f(b));
printf("%1.5E\n",Itr)

%Simpson
h=(b-a)/2;
Isimp = (h/3)*(f(a)+4*f((a+b)/2)+f(b));
printf("%1.5E\n",Isimp)