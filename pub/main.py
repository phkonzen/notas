#!/usr/bin/python3
'''
Constroi/atualiza o __site__ 
das notas de aula.

Autor: Pedro H A Konzen - 05/2018
Modificado: 05/2022
'''

#pacotes do Python
import os
from multiprocessing import Pool

#classes
from index import *
from politica import *
from sitemap import *
from analisematematicai import *
from calculoi import *
from ead import *
from edo import *
from matematicanumerica import *
from matematicanumericaparalela import *
from matematicanumericaavancada import *
from metodoelementosfinitos import *
from precalculo import *
from vetores import *
from geometriaanalitica import *
from minicalcpy import *
from minipython import *

#pastas temporárias
odir = '.docs'
os.system('mkdir -p '+odir)
os.system('rm -rvf '+odir+'/*')

srcdir = '.src'
os.system('mkdir -p '+srcdir)
os.system('rm -rvf '+srcdir+'/*')

#fontawesome6
os.system('cp -rvf fontawesome ' + odir + '/')

#pics
os.system('cp -rvf pics ' + odir + '/')

#index.html
index = Index(odir)
index.build()

#politica.html
politica = Politica(odir)
politica.build()

#contato.html
os.system('cp contato.html '+odir+'/')

#copia src para pasta temporária
os.system('cp -rvf ../src/* '+srcdir+'/')

#del o site antigo
os.system('rm -rvf ../docs/*')

#objs da cada nota

#ami = AnaliseMatematicaI(srcdir,odir)
ci = CalculoI(srcdir,odir)
ead = EaD(srcdir,odir)
edo = EDO(srcdir,odir)
mn = MatematicaNumerica(srcdir,odir)
mnp = MatematicaNumericaParalela(srcdir,odir)
mna = MatematicaNumericaAvancada(srcdir,odir)
mef = MetodoElementosFinitos(srcdir,odir)
pc = PreCalculo(srcdir,odir)
v = Vetores(srcdir,odir)
ga = GeometriaAnalitica(srcdir,odir)
minicalcpy = MiniCalcPy(srcdir,odir)
minipy = MiniPython(srcdir,odir)

def build(id):
    id.build()

#região paralelizada
if __name__ == '__main__':
    p = Pool()
    p.map(build,[ci,ead,edo,mn,mnp,mna,mef,pc,v,ga,minicalcpy,minipy])

#cria o README.md do ../docs
os.system('cp docs_readme.md '+odir+'/README.md')

#fonts
os.system('cp -rvf fonts '+odir+'/')
    
#sitemap.txt
sm = SiteMap(odir)
sm.build()

#publica o novo site
os.system('cp -rvf '+odir+'/* ../docs/')
