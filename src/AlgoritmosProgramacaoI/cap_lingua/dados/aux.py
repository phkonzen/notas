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
