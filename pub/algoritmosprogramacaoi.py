#!/usr/bin/python3
'''
Publica as notas de 

Algoritmos e Programação I.

notas/src/AlgoritmosProgramacaoI

Autor: Pedro H A Konzen
'''

import os

from notas import *

class AlgoritmosProgramacaoI(Notas):
    
    def __init__(self,srcdir,odir):
        super().__init__()
        self.srcdir = srcdir
        self.odir = odir
        self.ebook = 'https://a.co/d/eRjID1A'

        self.folder_notas = 'AlgoritmosProgramacaoI'
        self.titulo_notas = 'Algoritmos e Programação I'

        
    # def make_pdf(self):
    #     os.chdir(self.srcdir+'/AlgoritmosProgramacaoI')
    #     os.system('make clean')
    #     os.system('make pdf')
    #     os.chdir('../..')

    # def make_html(self):
    #     os.chdir(self.srcdir+'/AlgoritmosProgramacaoI')
    #     os.system('make clean')
    #     os.system('make html')
    #     os.chdir('../..')
        
    # def build(self):
    #     #html
    #     self.make_html()
    #     self.goodies(self.srcdir+'/AlgoritmosProgramacaoI/html',\
    #                      'Algoritmos e Programação I', 'AlgoritmosProgramacaoI')
        
    #     os.system('rm -rvf '+self.odir+'/AlgoritmosProgramacaoI')
    #     os.system('mv '+self.srcdir+'/AlgoritmosProgramacaoI/html'\
    #                   +' '+self.odir+'/AlgoritmosProgramacaoI')

    #     #pdf
    #     self.make_pdf()
    #     os.system('mv '+self.srcdir+'/AlgoritmosProgramacaoI/main.pdf'\
    #               +' '+self.odir+'/AlgoritmosProgramacaoI/')
