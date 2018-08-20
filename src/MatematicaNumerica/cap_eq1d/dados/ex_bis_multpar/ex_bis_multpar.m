pkg load symbolic
syms x
f = (2*x.^3-1.4*x.^2-0.98*x+0.686).*exp(x^2)-...
    (x.^3-0.7*x.^2-0.49*x+0.343);
fl = matlabFunction(diff(f));

TOL=1e-3;
a=0.5;
b=1.0;
x=(a+b)/2;
printf("%d %1.4E %1.4E %1.4E %d\n",...
       1,a,b,x,sign(fl(a)*fl(x)));
for k=2:10
  if ((fl(x)==0) | ((b-a)/2<TOL))
    disp('convergiu')
    break;
  elseif (sign(fl(a)*fl(x))<0)
    b=x;
  else
    a=x;
  end
  x=(a+b)/2;
  printf("%d %1.4E %1.4E %1.4E %d\n",...
         k,a,b,x,sign(fl(a)*fl(x)));
endfor
