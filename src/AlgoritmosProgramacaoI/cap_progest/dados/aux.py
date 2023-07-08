print('p(x) = (x-a)(bx^2 + cx + d)')
# entrada de dados
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
d = float(input('Digite o valor de d: '))

# cálculo das raízes
x1 = a
print(f'x1 = {x1}')
if (b != 0.):
    delta = c**2 - 4*b*d
    x2 = (-c - delta**0.5)/(2*b)
    x3 = (-c + delta**0.5)/(2*b)
    print(f'x2 = {x2}')
    print(f'x3 = {x3}')
elif (c != 0.):
    x2 = -d/c
    print(f'x2 = {x2}')

