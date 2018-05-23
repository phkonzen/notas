#!/usr/bin/python3
'''
Publica as notas de Análise Matemática.

notas/src/AnaliseMatematica

Autor: Pedro H A Konzen - 05/2018
'''

import os

class AnaliseMatematica:
    
    def __init__(self,srcdir):
        self.srcdir = srcdir
        
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
        os.system('rm -rvf ../docs/AnaliseMatematica')
        os.system('mv '+self.srcdir+'/AnaliseMatematica/html'\
                      +' ../docs/AnaliseMatematica')
