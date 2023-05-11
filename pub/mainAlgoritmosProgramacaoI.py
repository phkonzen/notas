#!/usr/bin/python3
'''
Atualiza as notas de 
Algoritmos e Programação I
para o __site__.

Autor: Pedro H A Konzen - 05/2023
'''

# pacotes do Python
import os

# classes
from sitemap import *
from algoritmosprogramacaoi import *

# pastas temporárias
odir = '.docs'
os.system('rm -rvf '+odir)
os.system('cp -rvf ../docs '+odir)

srcdir = '.src'
os.system('mkdir -p '+srcdir)
os.system('rm -rvf '+srcdir+'/*')

# copia src para pasta temporária
os.system('cp -rvf ../src/* '+srcdir+'/')

# del as notas antigas
os.system('rm -rvf ../docs/AlgoritmosProgramacaoI')

# constroi as notas
mn = AlgoritmosProgramacaoI(srcdir,odir)
mn.build()

# make sitemap.txt
sm = SiteMap(odir)
sm.build()

# publica a atualização
os.system('rsync -av '+odir+'/* ../docs/')
