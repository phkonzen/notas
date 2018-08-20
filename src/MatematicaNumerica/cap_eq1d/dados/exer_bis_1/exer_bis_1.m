f = @(x) x.^3 .* sin(x) - cos(x);

a=0.5;
b=1;
x=(a+b)/2;
for k=2:7
  if (f(x)==0)
    disp('sol. encontrada')
    break;
  elseif (f(a)*f(x)>0)
    a=x;
  else
    b=x;
  end
  x=(a+b)/2;
endfor
printf("%1.6E\n",x)