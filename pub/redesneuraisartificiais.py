#!/usr/bin/python3
'''
Publica as notas de Redes Neurais Artificiais.

notas/src/RNA

Autor: Pedro H A Konzen - 06/2023
'''

import os

from notas import *

class RedesNeuraisArtificiais(Notas):
    
    def __init__(self,srcdir,odir):
        super().__init__()
        self.srcdir = srcdir
        self.odir = odir
        
    def make_pdf(self):
        os.chdir(self.srcdir+'/RedesNeuraisArtificiais')
        os.system('make clean')
        # self.tags2pdf(self.srcdir+'/MatematicaNumericaI')
        os.system('make pdf')
        os.chdir('../..')

    def make_html(self):
        os.chdir(self.srcdir+'/RedesNeuraisArtificiais')
        os.system('make clean')
        os.system('make html')
        os.chdir('../..')
        
    def build(self):
        #html
        self.make_html()
        self.goodies(self.srcdir+'/RedesNeuraisArtificiais/html',\
                         'Redes Neurais Artificiais', 'RedesNeuraisArtificiais')
        os.system('rm -rvf '+self.odir+'/RedesNeuraisArtificiais')
        os.system('mv '+self.srcdir+'/RedesNeuraisArtificiais/html'\
                      +' '+self.odir+'/RedesNeuraisArtificiais')

        #pdf
        self.make_pdf()
        os.system('mv '+self.srcdir+'/RedesNeuraisArtificiais/main.pdf'\
                  +' '+self.odir+'/RedesNeuraisArtificiais/')
