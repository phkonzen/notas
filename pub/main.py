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
from calculoi import *
from edo import *
from matematicanumerica import *
from metodoelementosfinitos import *
from vetoresgeometriaanalitica import *
from minicalcpy import *

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

#contato.html
os.system('cp contato.html '+odir+'/')

#copia src para pasta temporária
os.system('cp -rvf ../src/* '+srcdir+'/')

#del o site antigo
os.system('rm -rvf ../docs/*')

#cria o README.md do ../docs
os.system('cp docs_readme.md ../docs/README.md')

#objs da cada nota

#ami = AnaliseMatematicaI(srcdir,odir)
ci = CalculoI(srcdir,odir)
edo = EDO(srcdir,odir)
mn = MatematicaNumerica(srcdir,odir)
mef = MetodoElementosFinitos(srcdir,odir)
vgm = VetoresGeometriaAnalitica(srcdir,odir)
mini = MiniCalcPy(srcdir,odir)

def build(id):
    id.build()

#pallelized region
if __name__ == '__main__':
    p = Pool()
    p.map(build,[ci,edo,mn,mef,vgm,mini])

#make sitemap.txt
sm = SiteMap(odir)
sm.build()

#publica o novo site
os.system('cp -rvf '+odir+'/* ../docs/')
