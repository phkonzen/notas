f = @(x) sin(x+pi/4).^2-x.^3+pi*x.^2/4+5*pi^2*x/16+3*pi^3/64;

a=2; b=3;
x=(a+b)/2
printf("%d %1.4E %1.4E %1.4E %d\n",...
       1,a,b,x,sign(f(a))*sign(f(x)))
for k=2:10

  if (f(x) == 0)
    disp("sol. encontrada")
  elseif (sign(f(a))*sign(f(x)) == -1)
    b=x;
  else
    a=x;
  end
  
  x=(a+b)/2;
  printf("%d %1.4E %1.4E %1.4E %d\n",...
         k,a,b,x,sign(f(a))*sign(f(x)))
  
end