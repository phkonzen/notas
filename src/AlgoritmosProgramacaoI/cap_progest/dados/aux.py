x = float(input('Digite um número não negativo para x:\n'))
r = 1
k = 0
print(f'{k}: {r}')
while (k < 5):
    r = 0.5*(r + x/r)
    k = k + 1
    print(f'{k}: {r}')
print(f'sqrt({x}) = {r}')


n = int(input('Digite um número inteiro n:\n'))
m = int(input('Digite um número inteiro m>n:\n'))
soma = 0
for i in range(n,m+1):
    soma = soma + i
print(f'n+...+m = {soma}')

# entrada de dados
x = float(input('Digite o valor de x:\n'))
op = input('Digite uma das operações +, -, * ou /:\n')
y = float(input('Digite o valor de y:\n'))

# calcula
if (op == '+'):
    print(f'{x} ' + op + f' {y} = {x+y}')
elif (op == '-'):
    print(f'{x} ' + op + f' {y} = {x-y}')
elif (op == '*'):
    print(f'{x} ' + op + f' {y} = {x*y}')
elif (op == '/'):
    print(f'{x} ' + op + f' {y} = {x/y}')
else:
    print('Desculpa, não entendi!')



# entrada de dados
print('c1: (x-a1)**2 + (y-b1)**2 = r1')
a1 = float(input('Digite o valor de a1:\n'))
b1 = float(input('Digite o valor de b1:\n'))
r1 = float(input('Digite o valor de r1:\n'))
print('c2: (x-a2)**2 + (y-b2)**2 = r1')
a2 = float(input('Digite o valor de a2:\n'))
b2 = float(input('Digite o valor de b2:\n'))
r2 = float(input('Digite o valor de r2:\n'))

# verificações
if (((a1==a2) and (b1==b2)) and (r11==r2)):
    print('c1 = c2')
else:
    # distância entre os centros
    dist = ((a2-a1)**2 + (b2-b1)**2)**0.5
    if (abs(dist - (r1+r2)) < 1e-15):
        print('c1 & c2 têm um único ponto de interseção.')
    elif (dist < r1+r2):
        print('c1 & c2 têm dois pontos de interseção.')
    else:
        print('c1 & c2 não tem ponto de interseção.')

# entrada de dados
print('r1: a1*x + b1 = 0')
a1 = float(input('Digite o valor de a1:\n'))
b1 = float(input('Digite o valor de b1:\n'))
print('r2: a2*x + b2 = 0')
a2 = float(input('Digite o valor de a2:\n'))
b2 = float(input('Digite o valor de b2:\n'))

# resultado
if (a1 == a2):
    if (b1 == b2):
        print('r1 = r2')
    else:
        print('r1 // r2 e r1 != r2')
else:
    x = (b1-b2)/(a2-a1)
    y = a1*x + b1
    print('Ponto de interseção: ({x}, {y}).')





# entrada de dados
print('Circunferência c:')
a = float(input('Digite o valor de a:\n'))
b = float(input('Digite o valor de b:\n'))
r = float(input('Digite o valor de r:\n'))
print('Ponto (x, y):')
x = float(input('Digite o valor de x:\n'))
y = float(input('Digite o valor de y:\n'))

# resultado
if ((x-a)**2 + (y-b)**2 <= r):
    print(f'({x}, {y}) pertence ao disco.')
else:
    print(f'({x}, {y}) não pertence ao disco.')

# computação
if (a != 0):
    x = -b/a
    y = a*x + b
    print(f'Intercepta eixo-x em: ({x}, {y}).')

# entrada de dados
print('c1: (x-a1)**2 + (y-b1)**2 = r1')
a1 = float(input('Digite o valor de a1:\n'))
b1 = float(input('Digite o valor de b1:\n'))
r1 = float(input('Digite o valor de r1:\n'))
print('c2: (x-a2)**2 + (y-b2)**2 = r1')
a2 = float(input('Digite o valor de a2:\n'))
b2 = float(input('Digite o valor de b2:\n'))
r2 = float(input('Digite o valor de r2:\n'))
print('Ponto de interesse (x,y).')
x = float(input('Digite o valor de x:\n'))
y = float(input('Digite o valor de y:\n'))

# pertence ao disco c1?
c1 = (x-a1)**2 + (y-b1)**2 <= r1
# pertence ao disco c2?
c2 = (x-a2)**2 + (y-b2)**2 <= r2

# imprime resultado
if (c1 and c2):
    print(f'({x}, {y}) pertence à interseção dos discos.')
elif (c1):
    print(f'({x},{y}) pertence ao disco c1.')
elif (c2):
    print(f'({x},{y}) pertence ao disco c2.')
else:
    print(f'({x},{y}) não pertence aos discos.')



# entrada de dados
print('Coeficientes da parábola')
print('a1*x**2 + a2*x + a3 = 0')
a1 = float(input('Digite o valor de a1:\n'))
a2 = float(input('Digite o valor de a2:\n'))
a2 = float(input('Digite o valor de a3:\n'))

print('Coeficientes da reta')
b1 = float(input('Digite o valor de b1:\n'))
b2 = float(input('Digite o valor de b2:\n'))

# discriminante da equação
# a1*x**2 + (a2-b1)*x + (a3-b2) = 0
delta = (a2-b1)**2 - 4*a1*(a3-b2)

# ponto(s) de interseção
if (delta == 0):
    x = (b1-a2)/(2*a1)
    y = b1*x + b2
    print('Ponto de interseção:')
    print(f'({x}, {y})')
elif (delta > 0):
    x1 = ((b1-a2) - delta**2)/(2*a1)
    y1 = b1*x1 + b2
    x2 = ((b1-a2) + delta**2)/(2*a1)
    y2 = b1*x2 + b2
    print('Pontos de interseção:')
    print(f'({x1}, {y1}), ({x2}, {y2})')
else:
    print('Não há ponto de interseção.')
    

# discriminante
delta = b**2 - 4*a*c

# raízes
if (delta > 0):
    # raízes distintas
    x1 = (-b - delta**0.5)/(2*a)
    x2 = (-b + delta**0.5)/(2*a)
    print('Raízes reais distintas:')
    print(f'x_1 = {x1}')
    print(f'x_2 = {x2}')
elif (delta == 0):
    # raiz dupla
    x = -b/(2*a)
    print('Raiz dupla:')
    print('x_1 = x_2 = {x}')
else:
    # raízes complexas
    # parte real
    rea = -b/(2*a)
    # parte imaginária
    img = (-delta)**0.5/(2*a)
    x1 = rea - img*1j
    x2 = rea + img*1j
    print('Raízes complexas:')
    print(f'x_1 = {x1}')
    print(f'x_2 = {x2}')


x = 0
if (x >= 0):
    y = 1
x += y
print(x)
