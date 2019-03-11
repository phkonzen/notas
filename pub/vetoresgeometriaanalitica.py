#!/usr/bin/python3
'''
Publica as notas de Matemática Numérica.

notas/src/VetoresGeometriaAnalitica

Autor: Pedro H A Konzen - 03/2019
'''

import os

from notas import *

class VetoresGeometriaAnalitica(Notas):
    
    def __init__(self,srcdir,odir):
        self.srcdir = srcdir
        self.odir = odir
        
    def make_pdf(self):
        os.chdir(self.srcdir+'/VetoresGeometriaAnalitica')
        os.system('make clean')
        os.system('make pdf')
        os.chdir('../..')

    def make_html(self):
        os.chdir(self.srcdir+'/VetoresGeometriaAnalitica')
        os.system('make clean')
        os.system('make html')
        os.chdir('../..')
        
    def build(self):
        #html
        self.make_html()
        self.goodies(self.srcdir+'/VetoresGeometriaAnalitica/html',\
                         'Vetores e Geometria Analítica', 'VetoresGeometriaAnalitica')
        os.system('rm -rvf '+self.odir+'/VetoresGeometriaAnalitica')
        os.system('mv '+self.srcdir+'/VetoresGeometriaAnalitica/html'\
                      +' '+self.odir+'/VetoresGeometriaAnalitica')

        #pdf
        self.make_pdf()
        os.system('mv '+self.srcdir+'/VetoresGeometriaAnalitica/main.pdf'\
                  +' '+self.odir+'/VetoresGeometriaAnalitica/')
