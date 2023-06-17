#início

# repetição: for
for n in {-3, -2, -1, 0, 1, 2, 3}:
    res = (n%2 == 0)
    print(f'{n} é par? ', res)
    
#término

# bloco: entrada de dados
base = float(input('Digite a base:\n'))
altura = float(input('Digite a altura\n'))

# bloco: computação da área
area = base*altura/2

# bloco: saída de dados
print(f'Área = {area}')

#fim

v = [-1, 0, 2]
w = [3, 1, 2]
# a)
vpw = [v[0] + w[0],
       v[1] + w[1],
       v[2] + w[2]]
print(f'a) v+w = {vpw}')
# b)
vmw = [v[0] - w[0],
       v[1] - w[1],
       v[2] - w[2]]
print(f'b) v-w = {vmw}')
# c)
vdw = v[0]*w[0] + \
      v[1]*w[1] + \
      v[2]*w[2]
print(f'c) v.w = {vdw}')
# d)
norm_v = (v[0]**2 + \
         v[1]**2 + \
         v[2]**2)**0.5
print(f'd) ||v|| = {norm_v:.2f}')
# e)
norm_vmw = (vmw[0]**2 + \
         vmw[1]**2 + \
         vmw[2]**2)**0.5
print(f'e) ||v-w|| = {norm_vmw:.2f}')





a = [0,1]
a.append(a[0]+a[1])
a.append(a[1]+a[2])
a.append(a[2]+a[3])
a.append(a[3]+a[4])
print(a)



X = {-2,1,3}
Y = {5,-1,2}
XxY = {(-2,5), (-2,-1), (-2,2), \
       (1,5), (1,-1), (1,2), \
       (3,5), (3,-1), (3,2)}
print(f'#(X x Y) = {len(XxY)}')

A = {-3,-1,0,1,6,7}
B = {-4,1,3,5,6,7}
C = {-5,-3,1,2,3,5}
# a)
a = A & B
print(f"a)\n A&B = {a}")
# b)
b = C | B
print(f"b)\n A|B = {b}")
# c)
c = C - A
print(f"c)\n C-A = {c}")
# d)
d = B & (A | C)
print(f"d)\n B&(A|C) = {d}")


# vértices do triangulo
tria = {'A': (0,0), 'B': (1,0), 'C': (0,1)}
# aresta AB
tria['AB'] = ((tria['B'][0] - tria['A'][0])**2 \
    + (tria['B'][1] - tria['A'][1])**2)**0.5
# aresta BC
tria['BC'] = ((tria['C'][0] - tria['B'][0])**2 \
    + (tria['C'][1] - tria['B'][1])**2)**0.5
# aresta AC
tria['AC'] = ((tria['C'][0] - tria['A'][0])**2 \
    + (tria['C'][1] - tria['A'][1])**2)**0.5
# novo dicionário
print(tria)


A = [[-1,1,2],
     [1,3,-1],
     [2,0,-1]]

v = [-1, 2, 1]
w = [3, -1, 4]
p = v[0]*w[0] \
    + v[1]*w[1] \
    + v[2]*w[2]
print(f'v.w = {p}')


s = input('Digite uma palavra:\n\t')
print(f'A palavra {s} tem {len(s)} letras.')


# entrada de dados
base = float(input('Entre com o valor da base:\n\t'))
altura = float(input('Entre com o valor da altura:\n\t'))

# cálculo da área
area = base*altura/2

# imprime a área
print(f'Área do triangulo de ')
print(f'\t base = {base:e}')
print(f'\t altura = {altura:e}')
print(f'é igual a {area:e}')

x = 3
print('É par?')
print(x % 2 == 0)

# ponto
x = 2
y = 0.5

# y >= 0 e y <= f(x) ?
resp1 = y >= 0 and y <= (x-1)**3
# y >= f(x) e y <= 0 ?
resp2 = y >= (x-1)**3 and y <= 0

# conclusão
print("O ponto está entre as curvas?")
print(resp1 or resp2)


# circunferência c1
a1 = 0
b1 = 0
r1 = 1

# circunferência c2
a2 = 1
b2 = 1
r2 = 1

# ponto obj
x = 0.5
y = 0.5

# está em c1?
em_c1 = (x-a1)**2 + (y-b1)**2 <= r1**2

# está em c2?
em_c2 = (x-a2)**2 + (y-b2)**2 <= r2**2

# está em c1 e c2?
resp = em_c1 and em_c2
print('O ponto está na interseção de c1 e c2?', resp)


# ponto
x = 1
y = 1

# centro circunferência
a = 0
b = 0
# raio circunferência
raio = 1

# verifica se está no disco
v = (x-a)**2 + (y-b)**2 <= raio**2

# imprime resposta
print('O ponto está no disco?', v)



# parametros
a1 = 1
a2 = -1
b1 = 1
b2 = -1
# ponto x de interseção
x_intercep = (b2-b1)/(a1-a2)
# ponto y de interceção
y_intercep = a1*x_intercep + b1
# imprime o resultado
print(f'x_i = {x_intercep:e}')
print(f'y_i = {y_intercep:e}')
