f = @(x) (2*x.^3-1.4*x.^2-0.98*x+0.686).*exp(-x.^2)-...
         (x.^3-0.7*x.^2-0.49*x+0.343).*exp(-x.^4);

a=-1; b=1;
x=(a+b)/2
printf("%d %1.4E %1.4E %1.4E %d\n",...
       1,a,b,x,sign(f(a)*f(x)))
for k=2:10

  if (f(x) == 0)
    disp("sol. encontrada")
  elseif (sign(f(a)*f(x)) == -1)
    b=x;
  else
    a=x;
  end
  
  x=(a+b)/2;
  printf("%d %1.4E %1.4E %1.4E %d\n",...
         k,a,b,x,sign(f(a)*f(x)))
  
end