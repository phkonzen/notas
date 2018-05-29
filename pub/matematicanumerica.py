#!/usr/bin/python3
'''
Publica as notas de Matemática Numérica.

notas/src/MatematicaNumerica

Autor: Pedro H A Konzen - 05/2018
'''

import os

from notas import *

class MatematicaNumerica(Notas):
    
    def __init__(self,srcdir,odir):
        self.srcdir = srcdir
        self.odir = odir
        
    def make_pdf(self):
        os.chdir(self.srcdir+'/MatematicaNumerica')
        os.system('make clean')
        os.system('make pdf')
        os.chdir('../..')

    def make_html(self):
        os.chdir(self.srcdir+'/MatematicaNumerica')
        os.system('make clean')
        os.system('make html')
        os.chdir('../..')
        
    def build(self):
        #html
        self.make_html()
        self.goodies(self.srcdir+'/MatematicaNumerica/html',\
                         'Matemática Numérica', 'MatematicaNumerica')
        os.system('rm -rvf '+self.odir+'/MatematicaNumerica')
        os.system('mv '+self.srcdir+'/MatematicaNumerica/html'\
                      +' '+self.odir+'/MatematicaNumerica')

        #pdf
        self.make_pdf()
        os.system('mv '+self.srcdir+'/MatematicaNumerica/main.pdf'\
                      +' '+self.odir+'/MatematicaNumerica/')
