rand("seed",0)
f = @(x) x*exp(-x^2);
a=0;
b=1;
n=100000;
s=0;
for i=1:n
  x=a + (b-a)*rand();
  s+=f(x);
endfor
s*=(b-a)/n;

ia=0.5-exp(-1)/2;
printf("%1.5E %1.1E\n",s,abs(ia-s))
