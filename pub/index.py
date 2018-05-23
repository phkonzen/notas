#!/usr/bin/python3
'''
index.html

Autor: Pedro H A Konzen - 05/2018
'''

class Index:
    
    def __init__(self,odir):
        self.odir = odir
        self.page = ''
        
    def empty_page(self):
        self.page += '<!DOCTYPE html>\n'
        self.page += '<html>\n'
        self.page += '</html>'

    def add_head(self):
        head = '<head>\n'
        head += '<title>Notas de aula</title>\n'
        head += '</head>\n'
        self.page = self.page.replace('<html>',head)

    def add_body(self):
        body = '<body>\n'
        body += '<p>Hello, you there!</p>\n'
        body += '</body>\n'
        self.page = self.page.replace('</html>',body)

    def build(self):
        self.empty_page()
        self.add_head()
        self.add_body()
        f = open(self.odir + '/index.html','w')
        f.write(self.page)
        f.close()
