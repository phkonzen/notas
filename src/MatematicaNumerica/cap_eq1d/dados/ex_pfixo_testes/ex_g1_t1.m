g1 = @(x) 16/(5*pi^2)*(-sin(x+pi/4).^2+x.^3-pi*x.^2/4-3*pi^3/64);
x=-0.7;
for k=2:100
  x=f1(x);
endfor
x