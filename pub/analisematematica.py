#!/usr/bin/python3
'''
Publica as notas de Análise Matemática.

notas/src/AnaliseMatematica

Autor: Pedro H A Konzen - 05/2018
'''

import os

#classe mãe
from notas import *

class AnaliseMatematica(Notas):
    
    def __init__(self,srcdir,odir):
        self.srcdir = srcdir
        self.odir = odir
        
    def make_pdf(self):
        os.chdir(self.srcdir+'/AnaliseMatematica')
        os.system('make clean')
        os.system('make pdf')
        os.chdir('../..')

    def make_html(self):
        os.chdir(self.srcdir+'/AnaliseMatematica')
        os.system('make clean')
        os.system('make html')
        os.chdir('../..')
        
    def build(self):
        self.make_pdf()
        self.make_html()
        self.goodies(self.srcdir+'/AnaliseMatematica/html',
                         'Análise Matemática')
        os.system('rm -rvf '+self.odir+'/AnaliseMatematica')
        os.system('mv '+self.srcdir+'/AnaliseMatematica/html'\
                      +' '+self.odir+'/AnaliseMatematica')
        os.system('mv '+self.srcdir+'/AnaliseMatematica/main.pdf'\
                      +' '+self.odir+'/AnaliseMatematica/')
