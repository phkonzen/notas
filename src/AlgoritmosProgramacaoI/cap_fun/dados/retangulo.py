'''
Módulo com funcionalidades sobre
retângulos.
'''

import math as m

def perimetro(a, b):
    '''
    Perímetro de um retângulo de 
    lados a e b.

    Entrada
    -------
    a : float
    Comprimento de um dos lados.

    b : float
    Comprimento de outro dos lados.

    Saída
    -----
    p : float
    Perímetro do retângulo.
    '''

    p = a + b
    return p

def area(a, b):
    '''
    Área de um retângulo de 
    lados a e b.

    Entrada
    -------
    a : float
    Comprimento de um dos lados.

    b : float
    Comprimento de outro dos lados.

    Saída
    -----
    area : float
    Área do retângulo.
    '''

    area = a*b
    return area

def diagonal(a, b):
    '''
    Comprimento da diagonal de
    um retângulo de lados a e b.

    Entrada
    -------
    a : float
    Comprimento de um dos lados.

    b : float
    Comprimento de outro dos lados.

    Saída
    -----
    diag : float
    Diagonal do retângulo.
    '''

    diag = m.sqrt(a**2 + b**2)
    return diag
