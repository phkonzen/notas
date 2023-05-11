f = @(x) sin(x+pi/4).^2-x.^3+pi*x.^2/4+5*pi^2*x/16+3*pi^3/64;

TOL=1e-3;
a=2; b=3;
for k=1:10
  x=a-(b-a)/(f(b)-f(a))*f(a);
  printf("%d %1.4E %1.4E %1.4E %d\n",...
       k,a,b,x,sign(f(a))*sign(f(x)))

  if (f(x) == 0)
    disp("convergiu")
    break;
  elseif (sign(f(a))*sign(f(x)) == -1)
    b=x;
  else
    a=x;
  end  
end