f = @(x) (sin(x+2)-exp(-x.^2));

n=5;
w=pi/n;
s=0;
for i=1:n
  x = cos((2*i-1)*pi/(2*n));
  s+=f(x)*w;
endfor
printf("%1.5E\n",s)