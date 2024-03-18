#!/usr/bin/python3
'''
Publica as notas do 
Minicurso de C++ para Matemática.

notas/src/MiniCpp

Autor: Pedro H A Konzen - Out/2023
'''

import os

from notas import *

class MiniCpp(Notas):
    
    def __init__(self,srcdir,odir):
        super().__init__()
        self.srcdir = srcdir
        self.odir = odir
        
    def make_pdf(self):
        os.chdir(self.srcdir+'/MiniCpp')
        os.system('make clean')
        os.system('make pdf')
        os.chdir('../..')

    def make_html(self):
        os.chdir(self.srcdir+'/MiniCpp')
        os.system('make clean')
        os.system('make html')
        os.chdir('../..')
        
    def build(self):
        #html
        self.make_html()
        self.goodies(self.srcdir+'/MiniCpp/html',\
                         'Minicurso de C++ para Matemática', 'MiniCpp')
        os.system('rm -rvf '+self.odir+'/MiniCpp')
        os.system('mv '+self.srcdir+'/MiniCpp/html'\
                      +' '+self.odir+'/MiniCpp')

        #pdf
        self.make_pdf()
        os.system('mv '+self.srcdir+'/MiniCpp/main.pdf'\
                  +' '+self.odir+'/MiniCpp/')


    
