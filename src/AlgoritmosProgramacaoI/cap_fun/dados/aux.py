def inDisk(a=0, b=0, r=1, *pts):
    for pt in pts:
        if ((pt[0]-a)**2 + (pt[1]-b)**2 <= r**2):
            print(f'({pt[0]}, {pt[1]}) pertence ao disco.')
        else:
            print(f'({pt[0]}, {pt[1]}) não pertence ao disco.')


def EhPrimo(n):
    info = True
    for i in range(2,n//2+1):
        if (n % i == 0):
            info = False
            break
    return info

def primos(n=1, m=29):
    lista = []
    for x in range(n, m+1):
        if EhPrimo(x):
            lista.append(x)
    return lista

import math as m

def raizPoli1(a, b):
    '''
    ax + b = 0
    '''
    return {-b/a}

def raizPoli2(a, b, c):
    '''
    ax^2 + bx + c = 0
    '''
    delta = b**2 - 4*a*c
    x1 = (-b - m.sqrt(delta))/(2*a)
    x2 = (-b + m.sqrt(delta))/(2*a)
    return {x1, x2}

def raizPoli12(**coefs):
    if (len(coefs) == 2):
        return raizPoli1(coefs['a'], coefs['b'])
    elif (len(coefs) == 3):
        return raizPoli2(coefs['a'], coefs['b'], coefs['c'])
    else:
        raise Exception('Polinômio inválido.')

print('x - 2 = 0')
print(f'x = {raizPoli12(a=1, b=-2)}')

print('2x^2 - 3x + 1 = 0')
print(f'x = {raizPoli12(a=2, b=-3, c=1)}')




def fun(x, y):
    print(f'x = {x}')
    print(f'y = {y}')

    
def progAritm(a0, r, n=5):
    return [a0 + i*r for i in range(n+1)]
print(progAritm(1, 2))

y = 1
def fun(x=y):
    y = 2
    print(x)
fun()

def bigollo(n=5):
    fibo = [1]*n
    for i in range(2,n):
        fibo[i] = sum(fibo[i-2:i])
    return fibo

print(bigollo())

def fun(x, x0=0):
    glo x
    x = x - 1

x = 3
y = fun()
print(f'x = {x}')



import math as m

def fun(n):
    print('Na função:')
    print(f'\tn = {n}, id = {id(n)}')
    n = n + 1
    print(f'\tn = {n}, id = {id(n)}')
    return n

n = 1
print(f'n = {n}, id = {id(n)}')

m = fun(n)
print(f'n = {n}, id = {id(n)}')
print(f'm = {m}, id = {id(m)}')
