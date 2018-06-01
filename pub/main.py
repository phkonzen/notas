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
from matematicanumerica import *

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

#del o site antigo
os.system('rm -rvf ../docs/*')

#AnaliseMatematica
am = AnaliseMatematica(srcdir,odir)
am.build()

#AnaliseMatematica
mn = MatematicaNumerica(srcdir,odir)
mn.build()

#put the google verification code
os.system('cp googlee521115172992e66.html '+odir+'/')

#publica o novo site
os.system('cp -rvf '+odir+'/* ../docs/')
