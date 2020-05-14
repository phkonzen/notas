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
os.system('rm -rvf '+odir+'/*')

#index.html
index = Index(odir)
index.build()

# #contato.html
# os.system('cp contato.html '+odir+'/')

#publica o novo site
os.system('cp -rvf '+odir+'/* ../docs/')
