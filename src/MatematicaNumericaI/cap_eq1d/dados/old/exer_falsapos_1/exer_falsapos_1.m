f = @(x) x.^3 .* sin(x) - cos(x);

a=0.5;
b=1;
for k=1:5
  x = a - (b-a)/(f(b)-f(a))*f(a)
  if (f(x)==0)
    disp('sol. encontrada')
    break;
  elseif (f(a)*f(x)>0)
    a=x;
  else
    b=x;
  end
endfor
printf("%1.6E\n",x)