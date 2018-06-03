f = @(x) sin(x);
dfp = @(x,h) (f(x+h)-f(x-h))/(2*h);
x=pi/3;
h=1;
T=zeros(4,4);
for i=1:4
  T(i,1) = dfp(x,h/2^(i-1));
endfor
for j=2:4
  for i=j:4
    T(i,j) = T(i,j-1) ... 
           + (T(i,j-1)-T(i-1,j-1))/(4^(j-1)-1);
  endfor
endfor
for i=1:4
  printf("%1.5E %1.5E %1.5E %1.5E\n",T(i,:))
endfor