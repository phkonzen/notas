x = [-2.5 -1.3 0.2 1.7 2.3]';
y = [3.8 1.5 -0.7 -1.5 -3.2]';

A = [x ones(5,1)];
c = A\y;

printf('c = %1.5e\n',c)
printf('r = %1.5e\n',norm(y - polyval(c,x)))

xx = linspace(-2.6,2.4);
plot(x,y,'ro',...
     xx,polyval(c,xx));grid