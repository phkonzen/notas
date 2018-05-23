#!/usr/bin/python3
'''
Publica as notas de Matemática Numérica.

notas/src/MatematicaNumerica

Autor: Pedro H A Konzen - 05/2018
'''

import os

class MatematicaNumerica:
    
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
        self.make_pdf()
        self.make_html()
        os.system('rm -rvf '+self.odir+'/MatematicaNumerica')
        os.system('mv '+self.srcdir+'/MatematicaNumerica/html'\
                      +' '+self.odir+'/MatematicaNumerica')
        os.system('mv '+self.srcdir+'/MatematicaNumerica/main.pdf'\
                      +' '+self.odir+'/MatematicaNumerica/')
