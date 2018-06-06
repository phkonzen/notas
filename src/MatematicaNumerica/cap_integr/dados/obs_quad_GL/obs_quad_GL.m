pkg load miscellaneous
n=5;
Pn=legendrepoly(n);
dPn=polyder(Pn);
x=roots(Pn);
w=2./((1-x.^2).*(polyval(dPn,x)).^2);
printf("i xx_i w_i\n")
for i=1:n
  printf("%d %1.7E %1.7E\n",i,x(i),w(i))
endfor
