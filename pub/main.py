#!/usr/bin/python3
'''
Constroi o __site__ das notas de aula.

Autor: Pedro H A Konzen - 05/2018
'''

#pacotes do Python
import os

#classes
from index import *
from analisematematica import *

#pastas temporárias
odir = '.docs'
os.system('mkdir -p '+odir)
os.system('rm -rvf '+odir+'/*')

srcdir = '.src'
os.system('mkdir -p '+srcdir)
os.system('rm -rvf '+srcdir+'/*')

#index.html
index = Index(odir)
index.build()

#copia src para pasta temporária
os.system('cp -rvf ../src/* '+srcdir+'/')

#AnaliseMatematica
am = AnaliseMatematica(srcdir,odir)
am.build()
