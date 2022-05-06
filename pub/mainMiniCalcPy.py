#!/usr/bin/python3
'''
Atualiza as notas do minicurso de Cálculo com Python para o __site__.

Autor: Pedro H A Konzen - 10/2019
'''

# pacotes do Python
import os

# classes
from sitemap import *
from minicalcpy import *

# publica a atualização
os.system('rsync -av ../src/MiniCalcPy/*.ipynb ../docs/MiniCalcPy/')
