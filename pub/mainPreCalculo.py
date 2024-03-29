#!/usr/bin/python3
'''
Atualiza as notas de Pré-Cálculo para o __site__.

Autor: Pedro H A Konzen - 05/2022
Modificado: xx/xxxx
'''

# pacotes do Python
import os

# classes
from sitemap import *
from precalculo import *

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
os.system('rm -rvf ../docs/PreCalculo')

# constroi as notas
ci = PreCalculo(srcdir,odir)
ci.build()

# make sitemap.txt
sm = SiteMap(odir)
sm.build()

# publica a atualização
os.system('rsync -av '+odir+'/* ../docs/')
