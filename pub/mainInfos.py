#!/usr/bin/python3
'''
Atualiza apenas a infos.html

Autor: Pedro H A Konzen - 02/2024
'''

#pacotes do Python
import os

#classes
from infos import *

#pastas temporárias
odir = '.docs'
os.system('mkdir -p '+odir)
os.system('rm -rvf '+odir+'/infos.html')

#infos.html
infos = Infos(odir)
infos.build()

#fonts
os.system('cp -rvf fonts '+odir+'/')

# publica a atualização
os.system('rsync -av '+odir+'/* ../docs/')
