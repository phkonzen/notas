#!/usr/bin/python3
'''
Publica as notas de Matemática Numérica II.

notas/src/MatematicaNumericaII

Autor: Pedro H A Konzen - 04/2023
'''

import os

from notas import *

class MatematicaNumericaII(Notas):
    
    def __init__(self,srcdir,odir):
        super().__init__()
        self.srcdir = srcdir
        self.odir = odir
        
    def make_pdf(self):
        os.chdir(self.srcdir+'/MatematicaNumericaII')
        os.system('make clean')
        # self.tags2pdf(self.srcdir+'/MatematicaNumericaI')
        os.system('make pdf')
        os.chdir('../..')

    def make_html(self):
        os.chdir(self.srcdir+'/MatematicaNumericaII')
        os.system('make clean')
        os.system('make html')
        os.chdir('../..')
        
    def build(self):
        #html
        self.make_html()
        self.goodies(self.srcdir+'/MatematicaNumericaII/html',\
                         'Matemática Numérica II', 'MatematicaNumericaII')
        os.system('rm -rvf '+self.odir+'/MatematicaNumericaII')
        os.system('mv '+self.srcdir+'/MatematicaNumericaII/html'\
                      +' '+self.odir+'/MatematicaNumericaII')

        #pdf
        self.make_pdf()
        os.system('mv '+self.srcdir+'/MatematicaNumericaII/main.pdf'\
                  +' '+self.odir+'/MatematicaNumericaII/')
