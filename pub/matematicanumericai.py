#!/usr/bin/python3
'''
Publica as notas de Matemática Numérica I.

notas/src/MatematicaNumericaI

Autor: Pedro H A Konzen - 04/2023
'''

import os

from notas import *

class MatematicaNumericaI(Notas):
    
    def __init__(self,srcdir,odir):
        self.srcdir = srcdir
        self.odir = odir
        
    def make_pdf(self):
        os.chdir(self.srcdir+'/MatematicaNumericaI')
        os.system('make clean')
        os.system('make pdf')
        os.chdir('../..')

    def make_html(self):
        os.chdir(self.srcdir+'/MatematicaNumericaI')
        os.system('make clean')
        os.system('make html')
        os.chdir('../..')
        
    def build(self):
        #html
        self.make_html()
        self.goodies(self.srcdir+'/MatematicaNumericaI/html',\
                         'Matemática Numérica I', 'MatematicaNumericaI')
        os.system('rm -rvf '+self.odir+'/MatematicaNumericaI')
        os.system('mv '+self.srcdir+'/MatematicaNumericaI/html'\
                      +' '+self.odir+'/MatematicaNumericaI')

        #pdf
        self.make_pdf()
        os.system('mv '+self.srcdir+'/MatematicaNumericaI/main.pdf'\
                  +' '+self.odir+'/MatematicaNumericaI/')
