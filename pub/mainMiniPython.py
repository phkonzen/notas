#!/usr/bin/python3
'''
Atualiza as notas do
Minicurso de Python para Matemática.

Autor: Pedro H A Konzen - 09/2021
'''

# pacotes do Python
import os

# classes
from sitemap import *
from minipython import *

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
os.system('rm -rvf ../docs/MiniPython')

# constroi as notas
ci = MiniPython(srcdir,odir)
ci.build()

# make sitemap.txt
sm = SiteMap(odir)
sm.build()

# publica a atualização
os.system('rsync -av '+odir+'/* ../docs/')
