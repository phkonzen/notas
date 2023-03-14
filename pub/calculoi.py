#!/usr/bin/python3
'''
Publica as notas de Cálculo I.

notas/src/CalculoI

Autor: Pedro H A Konzen - 03/2019
Modificado: 03/2023
'''

import os

from notas import *

class CalculoI(Notas):
    
    def __init__(self,srcdir,odir):
        self.srcdir = srcdir
        self.odir = odir
        
    def make_pdf(self):
        os.chdir(self.srcdir+'/CalculoI')
        os.system('make clean')
        os.system('make pdf')
        os.chdir('../..')

    def make_html(self):
        os.chdir(self.srcdir+'/CalculoI')
        os.system('make clean')
        os.system('make html')
        os.chdir('../..')
        
    def build(self):
        #html
        self.make_html()
        self.goodies(self.srcdir+'/CalculoI/html',\
                         'Cálculo I', 'CalculoI')
        os.system('rm -rvf '+self.odir+'/CalculoI')
        os.system('mv '+self.srcdir+'/CalculoI/html'\
                      +' '+self.odir+'/CalculoI')

        #pdf
        self.make_pdf()
        os.system('mv '+self.srcdir+'/CalculoI/main.pdf'\
                  +' '+self.odir+'/CalculoI/')


    
