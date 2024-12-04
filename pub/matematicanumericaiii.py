#!/usr/bin/python3
'''
Publica as notas de Matemática Numérica III.

notas/src/MatematicaNumericaIII

Autor: Pedro H A Konzen - 11/2023
'''

import os

from notas import *

class MatematicaNumericaIII(Notas):
    
    def __init__(self,srcdir,odir):
        super().__init__()
        self.srcdir = srcdir
        self.odir = odir

        self.folder_notas = 'MatematicaNumericaIII'
        self.titulo_notas = 'Matemática Numérica III'

        
    # def make_pdf(self):
    #     os.chdir(self.srcdir+'/MatematicaNumericaIII')
    #     os.system('make clean')
    #     os.system('make pdf')
    #     os.chdir('../..')

    # def make_html(self):
    #     os.chdir(self.srcdir+'/MatematicaNumericaIII')
    #     os.system('make clean')
    #     os.system('make html')
    #     os.chdir('../..')
        
    # def build(self):
    #     #html
    #     self.make_html()
    #     self.goodies(self.srcdir+'/MatematicaNumericaIII/html',\
    #                      'Matemática Numérica III', 'MatematicaNumericaIII')
    #     os.system('rm -rvf '+self.odir+'/MatematicaNumericaIII')
    #     os.system('mv '+self.srcdir+'/MatematicaNumericaIII/html'\
    #                   +' '+self.odir+'/MatematicaNumericaIII')

    #     #pdf
    #     self.make_pdf()
    #     os.system('mv '+self.srcdir+'/MatematicaNumericaIII/main.pdf'\
    #               +' '+self.odir+'/MatematicaNumericaIII/')
