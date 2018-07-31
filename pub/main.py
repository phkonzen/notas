#!/usr/bin/python3
'''
Constroi o __site__ das notas de aula.

Autor: Pedro H A Konzen - 05/2018
'''

#pacotes do Python
import os
from multiprocessing import Pool

#classes
from index import *
from sitemap import *
from analisematematicai import *
from matematicanumerica import *
from metodoelementosfinitos import *

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

#cria o README.md do ../docs
os.system('cp docs_readme.md ../docs/README.md')

#objs da cada nota
am = AnaliseMatematicaI(srcdir,odir)
mn = MatematicaNumerica(srcdir,odir)
ef = MetodoElementosFinitos(srcdir,odir)

def build(id):
    id.build()

#pallelized region
if __name__ == '__main__':
    p = Pool()
    p.map(build,[am,mn,ef])

#make sitemap.txt
sm = SiteMap(odir)
sm.build()

#publica o novo site
os.system('cp -rvf '+odir+'/* ../docs/')
