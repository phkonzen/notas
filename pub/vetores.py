#!/usr/bin/python3
'''
Publica as notas de Vetores.

notas/src/Vetores

Autor: Pedro H A Konzen - 03/2020
'''

import os

from notas import *

class Vetores(Notas):
    
    def __init__(self,srcdir,odir):
        self.srcdir = srcdir
        self.odir = odir
        
    def make_pdf(self):
        os.chdir(self.srcdir+'/Vetores')
        os.system('make clean')
        os.system('make pdf')
        os.chdir('../..')

    def make_html(self):
        os.chdir(self.srcdir+'/Vetores')
        os.system('make clean')
        os.system('make html')
        os.chdir('../..')
        
    def build(self):
        #html
        self.make_html()
        self.goodies(self.srcdir+'/Vetores/html',\
                         'Vetores', 'Vetores')
        os.system('rm -rvf '+self.odir+'/Vetores')
        os.system('mv '+self.srcdir+'/Vetores/html'\
                      +' '+self.odir+'/Vetores')

        #pdf
        self.make_pdf()
        os.system('mv '+self.srcdir+'/Vetores/main.pdf'\
                  +' '+self.odir+'/Vetores/')
