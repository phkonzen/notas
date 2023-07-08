n = int(input('Digite um número natural n >= 1: '))

s = 0
for k in range(1, n+1):
    s += (-1)**(k+1)/k
    k += 1
print(f'ln(2) aprrox. {s}')

print('P = (x,y)')
x = float(input('Digite o valor de x: '))
y = float(input('Digite o valor de y: '))

if (((x >= -1.) and (x <= 2)) and
    (y >= x**2) and (y <= x+2)):
    print(f'P = ({x}, {y}) está entre as curvas.')
else:
    print(f'P = ({x}, {y}) não está entre as curvas.')


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

