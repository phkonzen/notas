pkg load miscellaneous
n=5;
Hn=hermitepoly(n);
dHn=polyder(Hn);
x=roots(Hn);
w=2^(n+1)*factorial(n)*sqrt(pi)./((polyval(dHn,x)).^2);
printf("i xx_i w_i\n")
for i=1:n
  printf("%1.7E %1.7E\n",x(i),w(i))
endfor
