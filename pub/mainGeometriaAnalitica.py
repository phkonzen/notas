#!/usr/bin/python3
'''
Atualiza as notas de Geometria Analítica para o __site__.

Autor: Pedro H A Konzen - 03/2020
'''

# pacotes do Python
import os

# classes
from sitemap import *
from geometriaanalitica import *

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
os.system('rm -rvf ../docs/GeometriaAnalitica')

# constroi as notas
ga = GeometriaAnalitica(srcdir,odir)
ga.build()

# make sitemap.txt
sm = SiteMap(odir)
sm.build()

# publica a atualização
os.system('rsync -av '+odir+'/* ../docs/')
