pkg load symbolic
syms x
f = @(x) sin(x+pi/4).^2-x.^3+pi*x.^2/4+5*pi^2*x/16+3*pi^3/64;
fl = function_handle(diff(f(x)));

TOL=1e-3;
a=-1;
b=0;
for k=1:15
  x=(a+b)/2;
  printf("%d %1.4E %1.4E %1.4E %d\n",...
       k,a,b,x,sign(fl(a))*sign(fl(x)));
  if ((fl(x)==0) | ((b-a)/2<TOL))
    disp('convergiu')
    break;
  elseif (sign(fl(a))*sign(fl(x))==-1)
    b=x;
  else
    a=x;
  end
endfor
