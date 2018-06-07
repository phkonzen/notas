pkg load miscellaneous
n=5;
Ln=laguerrepoly(n);
dLn=polyder(Ln);
x=roots(Ln);
w=1./(x.*(polyval(dLn,x)).^2);
printf("i xx_i w_i\n")
for i=1:n
  printf("%1.7E %1.7E\n",x(i),w(i))
endfor
