#!/usr/bin/python3
'''
Atualiza apenas o index.html

Autor: Pedro H A Konzen - 05/2020
'''

#pacotes do Python
import os

#classes
from index import *

#pastas temporárias
odir = '.docs'
os.system('mkdir -p '+odir)
os.system('rm -rvf '+odir+'/index.html')

#index.html
index = Index(odir)
index.build()

# images
os.system('cp -rvf pics '+odir+'/')

#fonts
os.system('cp -rvf fonts '+odir+'/')

#fontawesome
os.system('cp -rvf fontawesome '+odir+'/')

#contato.html
os.system('cp contato.html '+odir+'/')

# publica a atualização
os.system('rsync -av '+odir+'/* ../docs/')
