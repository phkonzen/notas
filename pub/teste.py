#!/usr/bin/python3
'''
Publica as notas de Teste.

notas/src/Teste

Autor: Pedro H A Konzen - 03/2023
Modificado: 
'''

import os

from notas import *

class Teste(Notas):
    
    def __init__(self,srcdir,odir):
        super().__init__()
        self.srcdir = srcdir
        self.odir = odir
        
    def make_pdf(self):
        os.chdir(self.srcdir+'/Teste')
        os.system('make clean')
        os.system('make pdf')
        os.chdir('../..')

    def make_html(self):
        os.chdir(self.srcdir+'/Teste')
        os.system('make clean')
        os.system('make html')
        os.chdir('../..')
        
    def build(self):
        #html
        self.make_html()
        self.goodies(self.srcdir+'/Teste/html',\
                         'Teste', 'Teste')
        os.system('rm -rvf '+self.odir+'/Teste')
        os.system('mv '+self.srcdir+'/Teste/html'\
                      +' '+self.odir+'/Teste')

        #pdf
        self.make_pdf()
        os.system('mv '+self.srcdir+'/Teste/main.pdf'\
                  +' '+self.odir+'/Teste/')


    
