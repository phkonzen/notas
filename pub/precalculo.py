#!/usr/bin/python3
'''
Publica as notas de Pré-Cálculo.

notas/src/PreCalculo

Autor: Pedro H A Konzen - 05/2022
Modificado: xx/xxxx
'''

import os

from notas import *

class PreCalculo(Notas):
    
    def __init__(self,srcdir,odir):
        super().__init__()
        self.srcdir = srcdir
        self.odir = odir
        
    def make_pdf(self):
        os.chdir(self.srcdir+'/PreCalculo')
        os.system('make clean')
        os.system('make pdf')
        os.chdir('../..')

    def make_html(self):
        os.chdir(self.srcdir+'/PreCalculo')
        os.system('make clean')
        os.system('make html')
        os.chdir('../..')
        
    def build(self):
        #html
        self.make_html()
        self.goodies(self.srcdir+'/PreCalculo/html',\
                         'Pré-Cálculo', 'Pré-Cálculo')
        os.system('rm -rvf '+self.odir+'/PreCalculo')
        os.system('mv '+self.srcdir+'/PreCalculo/html'\
                      +' '+self.odir+'/PreCalculo')

        #pdf
        self.make_pdf()
        os.system('mv '+self.srcdir+'/PreCalculo/main.pdf'\
                  +' '+self.odir+'/PreCalculo/')


    
