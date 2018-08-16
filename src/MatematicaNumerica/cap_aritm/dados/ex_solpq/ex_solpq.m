function [r1,r2] = ex_solpq(a,b,c)
  aux = -0.5 * (b + sign(b)*sqrt(b^2-4*a*c));
  r1 = aux/a;
  r2 = c/aux;
endfunction