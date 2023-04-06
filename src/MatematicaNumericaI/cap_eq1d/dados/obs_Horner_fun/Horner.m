function [y,dy] = Horner(p,x0)
  n = length(p);
  y =p(1);
  dy=y;
  for k=2:n-1
    y=p(k)+y*x0;
    dy=y+dy*x0;
  endfor
  y=p(n)+y*x0;
endfunction
