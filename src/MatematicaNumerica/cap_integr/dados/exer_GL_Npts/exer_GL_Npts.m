pkg load miscellaneous

function [x,w] = quadGL(n)
  Pn=legendrepoly(n);
  dPn=polyder(Pn);
  x=roots(Pn);
  w=2./((1-x.^2).*(polyval(dPn,x)).^2);
endfunction

#a)
n=5;
[x,w] = quadGL(n);
s=0;
for i=1:n
  s+=w(i)*f(x(i));
endfor
printf("%1.5E\n",s)

#b)
n=10;
[x,w] = quadGL(n);
s=0;
for i=1:n
  s+=w(i)*f(x(i));
endfor
printf("%1.5E\n",s)

#b)
n=20;
[x,w] = quadGL(n);
s=0;
for i=1:n
  s+=w(i)*f(x(i));
endfor
printf("%1.5E\n",s)
