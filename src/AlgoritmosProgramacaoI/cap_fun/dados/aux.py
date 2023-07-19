import math as m

def raizes(a, b, c):
    '''
    Computa as raízes de
    p(x) = ax^2 + bx + c

    Entrada
    -------
    a : float
    Coeficiente do termo quadrático.
    Atenção! Deve ser diferente de zero.

    b : float 
    Coeficiente do termo linear.

    c: float
    Coeficiente do termo constante.

    Saída
    -----
    x1 : float
    Uma raíz do polinômio.

    x2 : float
    Outra raíz do polinômio.
    Atenção! No caso de raiz dupla,
    x1 == x2.
    '''

    # auxiliares
    _2a = 2*a
    _b2a = -b/_2a

    # discriminante
    delta = b**2 - 4*a*c

    # raízes
    if (delta > 0):
        x1 = _b2a + m.sqrt(delta)/_2a
        x2 = _b2a - m.sqrt(delta)/_2a
        return x1, x2
    elif (delta < 0):
        img = m.sqrt(-delta)/_2a
        x1 = _b2a + img*1j
        return x1, x1.conjugate()
    else:
        return _b2a, _b2a
    

# def fun
def areaCirc(r):
    area = m.pi * r**2
    return area
    
# entrada de dados
raio1 = float(input('Digite o raio da 1. circ.:\n'))
raio2 = float(input('Digite o raio da 2. circ.:\n'))

print(f'Circunferência de raio = {raio1}')
area1 = areaCirc(raio1)
print(f'\tárea = {area1}')

print(f'Circunferência de raio = {raio2}')
area2 = areaCirc(raio2)
print(f'\tárea = {area2}')


import random

def randImpar(m=51):
    '''
    Retorna um número randômico
    ímpar entre 1 e m (incluídos).

    Entrada
    -------
    m : int
    Maior inteiro ímpar que pode ser 
    gerado. Padrão: m = 51.

    Saída
    -----
    n : int
    Número randômico ímpar.
    '''
    n = random.randint(0, m-1)
    if (n % 2 != 0):
        return n
    else:
        return n+1

# entrada de dados
n = int(input('Digite o tamanho da lista:\n'))

# gera a lista
lista = [0]*n
for i in range(n):
    lista[i] = randImpar()

# calcula a média
soma = sum(lista)
media = soma/len(lista)

# imprime o resultados
print(f'média = {media}')

