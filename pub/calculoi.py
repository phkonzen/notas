#!/usr/bin/python3
'''
Publica as notas de Cálculo I.

notas/src/CalculoI

Autor: Pedro H A Konzen - 03/2019
Modificado: 12/2024
'''

import os

from notas import *

class CalculoI(Notas):
    
    def __init__(self, srcdir, odir):
        super().__init__()
        self.srcdir = srcdir
        self.odir = odir

        self.folder_notas = 'CalculoI'
        self.titulo_notas = 'Cálculo I'
        
    # def make_pdf(self):
    #     os.chdir(self.srcdir+'/CalculoI')
    #     os.system('make -B pdf')
    #     os.chdir('../..')

    # def make_html(self):
    #     os.chdir(self.srcdir+'/CalculoI')
    #     os.system('rm -r html/*')
    #     os.system('make -B html')
    #     os.chdir('../..')

    # def make_html_mobile(self):
    #     os.chdir(self.srcdir+'/CalculoI')
    #     os.system('rm -r html-mobile/*')
    #     os.system('make -B html-mobile')
    #     os.chdir('../..')

    # def build(self):
    #     #html
    #     self.make_html()
    #     self.make_html_mobile()
    #     self.goodies(self.srcdir+'/CalculoI/html',\
    #                      'Cálculo I', 'CalculoI')
    #     os.system('rm -rvf '+self.odir+'/CalculoI')
    #     os.system('mv '+self.srcdir+'/CalculoI/html'\
    #                   +' '+self.odir+'/CalculoI')

    #     #pdf
    #     self.make_pdf()
    #     os.system('mv '+self.srcdir+'/CalculoI/main.pdf'\
    #               +' '+self.odir+'/CalculoI/')


    
