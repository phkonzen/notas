#!/usr/bin/python3
'''
Publica as notas do 
Minicurso de Python para Matemática.

notas/src/MiniPython

Autor: Pedro H A Konzen - 09/2021
'''

import os

from notas import *

class MiniPython(Notas):
    
    def __init__(self,srcdir,odir):
        super().__init__()
        self.srcdir = srcdir
        self.odir = odir
        self.ebook = 'https://www.amazon.com.br/dp/B0DMPQ24VY'

        self.folder_notas = 'MiniPython'
        self.titulo_notas = 'Minicurso de Python para Matemática'

        
    # def make_pdf(self):
    #     os.chdir(self.srcdir+'/MiniPython')
    #     os.system('make clean')
    #     os.system('make pdf')
    #     os.chdir('../..')

    # def make_html(self):
    #     os.chdir(self.srcdir+'/MiniPython')
    #     os.system('make clean')
    #     os.system('make html')
    #     os.chdir('../..')
        
    # def build(self):
    #     #html
    #     self.make_html()
    #     self.goodies(self.srcdir+'/MiniPython/html',\
    #                      'Python para Matemática', 'MiniPython')
    #     os.system('rm -rvf '+self.odir+'/MiniPython')
    #     os.system('mv '+self.srcdir+'/MiniPython/html'\
    #                   +' '+self.odir+'/MiniPython')

    #     #pdf
    #     self.make_pdf()
    #     os.system('mv '+self.srcdir+'/MiniPython/main.pdf'\
    #               +' '+self.odir+'/MiniPython/')


    
