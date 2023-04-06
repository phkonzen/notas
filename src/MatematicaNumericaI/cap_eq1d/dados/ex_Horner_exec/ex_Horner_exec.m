p = [1 -3 0 4];
x0=1;

q = zeros(4,1);
q(1)=p(1);
for k=2:4
  q(k)=p(k)+q(k-1)*x0;
endfor
q(4)
