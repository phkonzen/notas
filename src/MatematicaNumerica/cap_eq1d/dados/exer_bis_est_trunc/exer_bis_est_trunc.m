f = @(x) (x-0.577)^3 .* sin(x) - (x - 0.577).^2 .* cos(x);

a=0.5;
b=1;
x=(a+b)/2;

%est trunc
kconv = ceil(log2((b-a)/1e-4))

for k=2:kconv
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
printf("%1.5E\n",x)