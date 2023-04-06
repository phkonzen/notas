f = @(x) (sin(x+2)-exp(-x^ 2))/(x^2+log(x+2))+x;

#a
dfp = @(x,h) (f(x+h)-f(x))/h;
x=2.5;
h=0.5;
T=zeros(3,3);
for i=1:3
  T(i,1) = dfp(x,h/2^(i-1));
endfor
for j=2:3
  for i=j:3
    T(i,j) = T(i,j-1) ... 
           + (T(i,j-1)-T(i-1,j-1))/(2^(j-1)-1);
  endfor
endfor
disp('a)')
for i=1:3
  printf("%1.5E %1.5E %1.5E\n",T(i,:))
endfor

#b
dfp = @(x,h) (f(x)-f(x-h))/h;
x=2.5;
h=0.5;
T=zeros(3,3);
for i=1:3
  T(i,1) = dfp(x,h/2^(i-1));
endfor
for j=2:3
  for i=j:3
    T(i,j) = T(i,j-1) ... 
           + (T(i,j-1)-T(i-1,j-1))/(2^(j-1)-1);
  endfor
endfor
disp('b)')
for i=1:3
  printf("%1.5E %1.5E %1.5E\n",T(i,:))
endfor

#c
dfp = @(x,h) (f(x+h)-f(x-h))/(2*h);
x=2.5;
h=0.5;
T=zeros(3,3);
for i=1:3
  T(i,1) = dfp(x,h/2^(i-1));
endfor
for j=2:3
  for i=j:3
    T(i,j) = T(i,j-1) ... 
           + (T(i,j-1)-T(i-1,j-1))/(4^(j-1)-1);
  endfor
endfor
disp('c)')
for i=1:3
  printf("%1.5E %1.5E %1.5E\n",T(i,:))
endfor