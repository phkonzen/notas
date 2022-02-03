#!/usr/bin/python3
'''
Publica as notas de Matemática Numérica Avancada.

notas/src/MatematicaNumericaAvancada

Autor: Pedro H A Konzen - 02/2022
'''

import os

from notas import *

class MatematicaNumericaAvancada(Notas):
    
    def __init__(self,srcdir,odir):
        self.srcdir = srcdir
        self.odir = odir
        
    def make_pdf(self):
        os.chdir(self.srcdir+'/MatematicaNumericaAvancada')
        os.system('make clean')
        os.system('make pdf')
        os.chdir('../..')

    def make_html(self):
        os.chdir(self.srcdir+'/MatematicaNumericaAvancada')
        os.system('make clean')
        os.system('make html')
        os.chdir('../..')
        
    def build(self):
        #html
        self.make_html()
        self.goodies(self.srcdir+'/MatematicaNumericaAvancada/html',\
                         'Matemática Numérica Avançada', 'MatematicaNumericaAvancada')
        os.system('rm -rvf '+self.odir+'/MatematicaNumericaAvancada')
        os.system('mv '+self.srcdir+'/MatematicaNumericaAvancada/html'\
                      +' '+self.odir+'/MatematicaNumericaAvancada')

        #pdf
        self.make_pdf()
        os.system('mv '+self.srcdir+'/MatematicaNumericaAvancada/main.pdf'\
                  +' '+self.odir+'/MatematicaNumericaAvancada/')
