#a) $(101101,00101)_2$ para base b=4
disp("a) b=2 -> b=10")
x = 2^6+2^4+2^3+2^0+2^-3+2^-5
disp("a) b=10 -> b=4 (parte inteira)")
I = fix(x)
d = mod(I,4), I=fix(I/4)
d = mod(I,4), I=fix(I/4)
d = mod(I,4), I=fix(I/4)
d = mod(I,4), I=fix(I/4)
disp("a) b=10 -> b=4 (parte fracionaria)")
F = x-fix(x)
d = fix(F*4), F = F*4-d
d = fix(F*4), F = F*4-d
d = fix(F*4), F = F*4-d


#b) $(23,1)_4$
x = 2*4^1 + 3*4^0 + 1*4^-1
x = 2*(2^2)^1 + (2+1)*(2^2)^0 + 1*(2^2)^-1
x = 2^3 + 2^1 + 2^0 + 2^-2
