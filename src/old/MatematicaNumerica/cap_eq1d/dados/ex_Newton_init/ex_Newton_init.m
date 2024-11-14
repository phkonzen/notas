f = @(x) (x-1).*exp(-x.^2);
fl = @(x) (1-2*x.*(x-1)).*exp(-x.^2);

x1=0.5;
x2=1.5;
for k=2:7
    x1=x1-f(x1)/fl(x1);
    x2=x2-f(x2)/fl(x2);
    printf("%d %1.4E %1.4E\n",k,x1,x2)
end

