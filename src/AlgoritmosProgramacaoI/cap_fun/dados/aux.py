import math as m

def raizFunAfim(a, b):
    '''
    Computa a raiz de
    f(x) = ax + b

    Entrada
    -------
    a : float
    Coeficiente angular.

    b : float
    Coeficiente linear.

    Saída
    -----
    x : float
    Raiz de f(x).
    '''
    
    try:
        x = -b/a
    except ZeroDivisionError:
        raise ZeroDivisionError('coef. angular deve ser != 0.')

    return x

# entrada de dados
try:
    a = float(input('Coef. angular: '))
except ValueError:
    raise ValueError('Número inválido.')

try:
    b = float(input('Coef. linear: '))
except ValueError:
    raise ValueError('Número inválido.')

# raiz
raiz = raizFunAfim(a, b)

# imprime
print(f'raiz = {raiz}')

    
    

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

    try:
        _b2a = -b/_2a
    except:
        raise Exception('número inválido')

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

