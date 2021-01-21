#!/usr/bin/python3
'''
Publica as notas de Matemática Numérica Paralela.

notas/src/MatematicaNumericaParalela

Autor: Pedro H A Konzen - 01/2021
'''

import os

from notas import *

class MatematicaNumericaParalela(Notas):
    
    def __init__(self,srcdir,odir):
        self.srcdir = srcdir
        self.odir = odir
        
    def make_pdf(self):
        os.chdir(self.srcdir+'/MatematicaNumericaParalela')
        os.system('make clean')
        os.system('make pdf')
        os.chdir('../..')

    def make_html(self):
        os.chdir(self.srcdir+'/MatematicaNumericaParalela')
        os.system('make clean')
        os.system('make html')
        os.chdir('../..')
        
    def build(self):
        #html
        self.make_html()
        self.goodies(self.srcdir+'/MatematicaNumericaParalela/html',\
                         'Matemática Numérica Paralela', 'MatematicaNumericaParalela')
        os.system('rm -rvf '+self.odir+'/MatematicaNumericaParalela')
        os.system('mv '+self.srcdir+'/MatematicaNumericaParalela/html'\
                      +' '+self.odir+'/MatematicaNumericaParalela')

        #pdf
        self.make_pdf()
        os.system('mv '+self.srcdir+'/MatematicaNumericaParalela/main.pdf'\
                  +' '+self.odir+'/MatematicaNumericaParalela/')
