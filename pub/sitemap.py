#!/usr/bin/python3
'''
sitemap.txt

Autor: Pedro H A Konzen - 05/2018
'''

import os

class SiteMap:
    
    def __init__(self,odir):
        self.odir = odir
        self.site = 'https://phkonzen.github.io/notas'
        self.sitemap = ''
        
    def build(self):
        pages = []
        for (dirpath, dirnames, filenames) in os.walk(self.odir):
            for fn in filenames:
                pages.append(dirpath+'/'+fn)
                
        for pp in pages:
            fn,ext = os.path.splitext(pp)
            if (ext == '.html'):
                self.sitemap += self.site+pp[5:]+'\n'
        
        f = open(self.odir + '/sitemap.txt','w')
        f.write(self.sitemap)
        f.close()
