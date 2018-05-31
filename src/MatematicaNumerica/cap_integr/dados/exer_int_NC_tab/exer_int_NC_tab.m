x = [2 2.1 2.2 2.3 2.4 2.5]';
y = [1.86 1.90 2.01 2.16 2.23 2.31]';

#a
h=0.2;
Ipm = h*y(3);
printf("%1.5E\n",Ipm)

#b
h=0.5;
Itr = h/2*(y(1)+y(6));
printf("%1.5E\n",Itr)

#c
h=0.2;
Isimp = h/3*(y(1)+4*y(3)+y(5));
printf("%1.5E\n",Isimp)