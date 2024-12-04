#!/usr/bin/python3
'''
Publica as notas de EDO.

notas/src/EDO

Autor: Pedro H A Konzen
'''

import os

from notas import *

class EDO(Notas):
    
    def __init__(self,srcdir,odir):
        super().__init__()
        self.srcdir = srcdir
        self.odir = odir

        self.folder_notas = 'EDO'
        self.titulo_notas = 'Equações Diferenciais Ordinárias'

        
    # def make_pdf(self):
    #     os.chdir(self.srcdir+'/EDO')
    #     os.system('make clean')
    #     os.system('make pdf')
    #     os.chdir('../..')

    # def make_html(self):
    #     os.chdir(self.srcdir+'/EDO')
    #     os.system('make clean')
    #     os.system('make html')
    #     os.chdir('../..')

    # def build(self):
    #     #html
    #     self.make_html()
    #     self.goodies(self.srcdir+'/EDO/html',\
    #                      'EDO', 'EDO')
    #     os.system('rm -rvf '+self.odir+'/EDO')
    #     os.system('mv '+self.srcdir+'/EDO/html'\
    #                   +' '+self.odir+'/EDO')

    #     #pdf
    #     self.make_pdf()
    #     os.system('mv '+self.srcdir+'/EDO/main.pdf'\
    #               +' '+self.odir+'/EDO/')


    
