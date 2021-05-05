#!/usr/bin/python3
'''
Atualiza apenas a politica.html

Autor: Pedro H A Konzen - 05/2021
'''

#pacotes do Python
import os

#classes
from politica import *

#pastas temporárias
odir = '.docs'
os.system('mkdir -p '+odir)
os.system('rm -rvf '+odir+'/politica.html')

#index.html
politica = Politica(odir)
politica.build()

# publica a atualização
os.system('rsync -av '+odir+'/* ../docs/')
