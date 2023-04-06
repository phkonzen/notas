x = [-1 0 1]';
y = [-1 1 0.5]';

paux = poly([x(2) x(3)]);
L1 = paux/polyval(paux,x(1))

paux = poly([x(1) x(3)]);
L2 = paux/polyval(paux,x(2))

paux = poly([x(1) x(2)]);
L3 = paux/polyval(paux,x(3))

p = y(1)*L1 + y(2)*L2 + y(3)*L3