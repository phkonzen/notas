#!/usr/bin/python3
'''
Constroi/atualiza o __site__ 
das notas de aula.

Autor: Pedro H A Konzen - 05/2018
Modificado: 11/2024
'''

#pacotes do Python
import os
import sys
from multiprocessing import Pool

#classes
from index import *
from infos import *
from sitemap import *
# from analisematematicai import *
from algoritmosprogramacaoi import *
from calculoi import *
from ead import *
from edo import *
# from matematicanumerica import *
from matematicanumericai import *
from matematicanumericaii import *
from matematicanumericaiii import *
from matematicanumericaparalela import *
from matematicanumericaavancada import *
from metodoelementosfinitos import *
from precalculo import *
from redesneuraisartificiais import *
from vetores import *
from geometriaanalitica import *
from minicalcpy import *
from minipython import *
from minicpp import *

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

# infos.html
infos = Infos(odir)
infos.build()

# contato.html
os.system('cp contato.html '+odir+'/')

#copia src para pasta temporária
os.system('cp -rvf ../src/* '+srcdir+'/')

#del o site antigo
os.system('rm -rvf ../docs/*')

#objs da cada nota

#ami = AnaliseMatematicaI(srcdir,odir)
api = AlgoritmosProgramacaoI(srcdir,odir)
ci = CalculoI(srcdir,odir)
ead = EaD(srcdir,odir)
edo = EDO(srcdir,odir)
# mn = MatematicaNumerica(srcdir,odir)
mni = MatematicaNumericaI(srcdir,odir)
mnii = MatematicaNumericaII(srcdir,odir)
mniii = MatematicaNumericaIII(srcdir,odir)
mnp = MatematicaNumericaParalela(srcdir,odir)
mna = MatematicaNumericaAvancada(srcdir,odir)
mef = MetodoElementosFinitos(srcdir,odir)
pc = PreCalculo(srcdir,odir)
rna = RedesNeuraisArtificiais(srcdir,odir)
v = Vetores(srcdir,odir)
ga = GeometriaAnalitica(srcdir,odir)
minicalcpy = MiniCalcPy(srcdir,odir)
minipy = MiniPython(srcdir,odir)
minicpp = MiniCpp(srcdir,odir)

def build(id):
    id.build()

#região paralelizada
if __name__ == '__main__':
    p = Pool(processes=6)
    p.map(build,[api,
                 ci,
                 ead,
                 edo,
#                 mn,
                 mni,
                 mnii,
                 mniii,                 
                 mnp,
                 mna,
                 mef,
                 pc,
                 rna,
                 v,
                 ga,
                 minicalcpy,
                 minipy,
                 minicpp])

#cria o README.md do ../docs
os.system('cp docs_readme.md '+odir+'/README.md')

# images
os.system('cp -rvf pics '+odir+'/')

#fonts
os.system('cp -rvf fonts '+odir+'/')
    
#sitemap.txt
sm = SiteMap(odir)
sm.build()

#publica o novo site
os.system('cp -rvf '+odir+'/* ../docs/')
