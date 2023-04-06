x = [0 1 1.5 2]';
y = exp(x);

paux = poly([x(2) x(3) x(4)]);
L1 = paux/polyval(paux,x(1))

paux = poly([x(1) x(3) x(4)]);
L2 = paux/polyval(paux,x(2))

paux = poly([x(1) x(2) x(4)]);
L3 = paux/polyval(paux,x(3))

paux = poly([x(1) x(2) x(3)]);
L4 = paux/polyval(paux,x(4))

p = y(1)*L1 + y(2)*L2 + y(3)*L3 + y(4)*L4
