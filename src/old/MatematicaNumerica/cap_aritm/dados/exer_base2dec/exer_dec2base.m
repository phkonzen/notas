#
disp("a) 45,5 base b=2")
disp("Parte inteira")
I = 45
d = mod(I,2), I = fix(I/2)
d = mod(I,2), I = fix(I/2)
d = mod(I,2), I = fix(I/2)
d = mod(I,2), I = fix(I/2)
d = mod(I,2), I = fix(I/2)
d = mod(I,2), I = fix(I/2)

disp("Parte fracionaria")
F = 0.5
d = fix(F*2), F=F*2-d

#
disp("b) 0,3 na base b=4")
F = 0.3
d = fix(F*4), F=F*4-d
d = fix(F*4), F=F*4-d
d = fix(F*4), F=F*4-d
d = fix(F*4), F=F*4-d
d = fix(F*4), F=F*4-d


