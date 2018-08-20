pkg load symbolic
syms x
f = (-x^2+1.154*x-0.332929)*cos(x)+x^2-1.154*x+0.332929;
fx = diff(f)
fl = function_handle(fx)

a=0.55;
b=0.65;
x=(a+b)/2;
x0=x;

for k=2:30
  if (fl(x)==0)
    disp('sol. encontrada')
    break;
  elseif (fl(a)*fl(x)>0)
    a=x;
  else
    b=x;
  end
  x=(a+b)/2;
  
  %ver. conv.
  if (abs(x-x0)<1e-4)
    disp("convergiu")
    break;
  end
  x0=x;
  
endfor
printf("%1.6E\n",x)