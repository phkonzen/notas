#!/usr/bin/python3
'''
Publica as notas de Geometrica Analítica.

notas/src/GeometriaAnalitica

Autor: Pedro H A Konzen - 03/2020
'''

import os

from notas import *

class GeometriaAnalitica(Notas):
    
    def __init__(self,srcdir,odir):
        super().__init__()
        self.srcdir = srcdir
        self.odir = odir
        
        self.folder_notas = 'GeometriaAnalitica'
        self.titulo_notas = 'Geometria Analítica'

    # def make_pdf(self):
    #     os.chdir(self.srcdir+'/GeometriaAnalitica')
    #     os.system('make clean')
    #     os.system('make pdf')
    #     os.chdir('../..')

    # def make_html(self):
    #     os.chdir(self.srcdir+'/GeometriaAnalitica')
    #     os.system('make clean')
    #     os.system('make html')
    #     os.chdir('../..')
        
    # def build(self):
    #     #html
    #     self.make_html()
    #     self.goodies(self.srcdir+'/GeometriaAnalitica/html',\
    #                      'Geometria Analítica', 'GeometriaAnalitica')
    #     os.system('rm -rvf '+self.odir+'/GeometriaAnalitica')
    #     os.system('mv '+self.srcdir+'/GeometriaAnalitica/html'\
    #                   +' '+self.odir+'/GeometriaAnalitica')

    #     #pdf
    #     self.make_pdf()
    #     os.system('mv '+self.srcdir+'/GeometriaAnalitica/main.pdf'\
    #               +' '+self.odir+'/GeometriaAnalitica/')
