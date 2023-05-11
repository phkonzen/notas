p = [1 -3 0 4];

x0=-2;
printf("%d %1.4E\n",1,x0)
for k=2:5
  [y,dy]=Horner(p,x0);
  x=x0-y/dy;
  printf("%d %1.4E %1.1E\n",k,x,abs(x-x0))
  x0=x;
endfor