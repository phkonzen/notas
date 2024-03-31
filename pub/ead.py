#!/usr/bin/python3
'''
Publica as notas de EaD.

notas/src/EaD

Autor: Pedro H A Konzen - 05/2020
'''

import os

from notas import *

class EaD(Notas):
    
    def __init__(self,srcdir,odir):
        super().__init__()
        self.srcdir = srcdir
        self.odir = odir
        
    def make_pdf(self):
        os.chdir(self.srcdir+'/EaD')
        os.system('make clean')
        os.system('make pdf')
        os.chdir('../..')

    def make_html(self):
        os.chdir(self.srcdir+'/EaD')
        os.system('make clean')
        os.system('make html')
        os.chdir('../..')
      
    def build(self):
        #html
        self.make_html()
        self.goodies(self.srcdir+'/EaD/html',\
                         'EaD', 'EaD')
        os.system('rm -rvf '+self.odir+'/EaD')
        os.system('mv '+self.srcdir+'/EaD/html'\
                      +' '+self.odir+'/EaD')

        #pdf
        self.make_pdf()
        os.system('mv '+self.srcdir+'/EaD/main.pdf'\
                  +' '+self.odir+'/EaD/')


    
