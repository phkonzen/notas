#!/usr/bin/python3
'''
Publica as notas de Análise Matemática I.

notas/src/AnaliseMatematicaI

Autor: Pedro H A Konzen - 05/2018
'''

import os

#classe mãe
from notas import *

class AnaliseMatematicaI(Notas):
    
    def __init__(self,srcdir,odir):
        self.srcdir = srcdir
        self.odir = odir
        
    def make_pdf(self):
        os.chdir(self.srcdir+'/AnaliseMatematicaI')
        os.system('make clean')
        os.system('make pdf')
        os.chdir('../..')

    def make_html(self):
        os.chdir(self.srcdir+'/AnaliseMatematicaI')
        os.system('make clean')
        os.system('make html')
        os.chdir('../..')
        
    def build(self):
        #html
        self.make_html()
        self.goodies(self.srcdir+'/AnaliseMatematicaI/html',
                         'Análise Matemática I', 'AnaliseMatematicaI')
        os.system('rm -rvf '+self.odir+'/AnaliseMatematicaI')
        os.system('mv '+self.srcdir+'/AnaliseMatematicaI/html'\
                      +' '+self.odir+'/AnaliseMatematicaI')

        #pdf
        self.make_pdf()
        os.system('mv '+self.srcdir+'/AnaliseMatematicaI/main.pdf'\
                      +' '+self.odir+'/AnaliseMatematicaI/')
