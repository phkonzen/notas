rand("seed",time())
f = @(x) (sin(x+2)-exp(-x^2))/(x^2+log(x+2));
a=-1;
b=1;

#num. max. iter.
n=999999;
#TOL
TOL=1e-3;
#cont. conv.
c=0;

#iteracoes
s0=0;
s1=0;
for i=1:n
  x=a + (b-a)*rand();
  s1*=(i-1);
  s1+=(b-a)*f(x);
  s1/=i;
  if (mod(i,10000)==0)
    if (abs(s1-s0)<TOL)
      c+=1;
    else
      s0=s1;
    endif
    if (c==2)
      break;
    endif
  endif
endfor
printf("%d %1.5E\n",i,s1)
