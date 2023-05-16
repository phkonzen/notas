b = float(input('Informe o valor da base do triângulo.\n'))
h = float(input('Informe o valor da altura do triângulo.\n'))
# cálculo da área
a = b*h/2
print(f'Área = {a}')

x = float(input('Entre com o valor de x: '))
if (x >= 0.):
    s = x/2
    for i in range(4):
        s = (s + x/s)/2
    print(f'Raiz aprox. de x = {s}')
else:
    print(f'Não existe!')
