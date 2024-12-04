#!/usr/bin/python3
'''
Publica as notas sobre o Método de
Elementos Finitos.

notas/src/MetodoElementosFinitos

Autor: Pedro H A Konzen - 07/2018
'''

import os

from notas import *

class MetodoElementosFinitos(Notas):
    
    def __init__(self,srcdir,odir):
        super().__init__()
        self.srcdir = srcdir
        self.odir = odir

        self.folder_notas = 'MetodoElementosFinitos'
        self.titulo_notas = 'Método de Elementos Finitos'

        
    # def make_pdf(self):
    #     os.chdir(self.srcdir+'/MetodoElementosFinitos')
    #     os.system('make clean')
    #     os.system('make pdf')
    #     os.chdir('../..')

    # def make_html(self):
    #     os.chdir(self.srcdir+'/MetodoElementosFinitos')
    #     os.system('make clean')
    #     os.system('make html')
    #     os.chdir('../..')
        
    # def build(self):
    #     #html
    #     self.make_html()
    #     self.goodies(self.srcdir+'/MetodoElementosFinitos/html',\
    #                      'Introdução ao Método de Elementos Finitos',
    #                      'MetodoElementosFinitos')
    #     os.system('rm -rvf '+self.odir+'/MetodoElementosFinitos')
    #     os.system('mv '+self.srcdir+'/MetodoElementosFinitos/html'\
    #                   +' '+self.odir+'/MetodoElementosFinitos')

    #     #pdf
    #     self.make_pdf()
    #     os.system('mv '+self.srcdir+'/MetodoElementosFinitos/main.pdf'\
    #                   +' '+self.odir+'/MetodoElementosFinitos/')
