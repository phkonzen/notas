#!/usr/bin/python3
'''
Publica as notas de Cálculo I.

notas/src/CalculoI

Autor: Pedro H A Konzen - 03/2019
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

    def goodies(self,htmldir,titulo_notas,srcref):
        #adiciona goodies.css
        f = open(htmldir+'/goodies.css','w')
        text = 'body {\n'
        text += 'font-family: Computer Modern Serif;\n'
        text += 'font-size: 2.3em;\n'
        text += '}\n\n'
        
        text += '.navbar-brand {\n'
        text += 'height: auto;\n'
        text += 'padding: 5px;\n'
        text += '}\n\n'
        
        f.write(text)
        f.close()
        
        #enxerta no __head__
        head = ''
        
        head += '<meta name="author" content="Pedro H A Konzen"/>\n'
        head += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n'
        head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n'
        head += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\n'
        head += '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        head += '<link rel="stylesheet" href="goodies.css" type="text/css">\n'

        #google tracking
        head += '\n<!-- Global site tag (gtag.js) - Google Analytics -->\n'
        head += '<script async src="https://www.googletagmanager.com/gtag/js?id=UA-17226092-2"></script>\n'
        head += '<script>\n'
        head += 'window.dataLayer = window.dataLayer || [];\n'
        head += 'function gtag(){dataLayer.push(arguments);}\n'
        head += 'gtag("js", new Date());\n'
        head += '\ngtag("config", "UA-17226092-2")\n';
        head += '</script>\n'

        
        head += '</head>\n'

        #enxerta no __body__ (top)
        body = '<body>\n\n'

        body += '<div class="row">\n'
        body += '<div class="col-xs-12 col-xs-offset-0 col-md-8 col-md-offset-2">\n'
        
        body += '\n\n<!-- begin: navbar -->\n'
        body += '<nav class="navbar navbar-default">\n'
        body += '<div class="container-fluid">\n'
        body += '<div class="navbar-header">\n'
        body += '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\n'
        body += '<span class="sr-only">Toggle navigation</span>\n'
        body += '<span class="icon-bar"></span>\n'
        body += '<span class="icon-bar"></span>\n'
        body += '<span class="icon-bar"></span>\n'
        body += '</button>\n'
        body += '<a class="navbar-brand" href="main.html">Notas de Aula<br/><small>'+titulo_notas+'<small/></a>\n'
        body += '</div>\n\n'

        body += '<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n'
        body += '<ul class="nav navbar-nav">\n'
        body += '<li><a href="https://github.com/phkonzen/notas">Repositório GitHub</a></li>\n'
        body += '<li><a href="main.pdf">Baixar PDF</a></li>\n'
        body += '<li><a href="https://mybinder.org/v2/gh/phkonzen/notas/master?filepath=%2Fsrc%2FCalculoI%2Fcalculoi.ipynb" target="_blank">Jupyter NB</a></li>\n'
        body += '<li><a href="../index.html">Outras Notas & Infos</a></li>\n'
        body += '</ul>\n'
        body += '</div><!-- /.navbar-collapse -->\n'
        body += '</div><!-- /.container-fluid -->\n'
        body += '</nav>\n'
        body += '\n\n<!-- end: navbar -->\n\n\n'

        #enxerta no __body__ (bottom)
        body_end = ''

        body_end += '</div><!-- div class="row" -->\n'
        body_end += '</div><!-- div class="col-xs-12 col-xs-offset-0 col-md-8 col-md-offset-2 -->\n'

        body_end += '</body>'

        #enxerta no __footer__
        foot = '<div class="ltx_page_logo">\n'
        foot += '<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Licença Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a><br />O texto acima está sob Licença <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/deed.pt_BR">Creative Commons Atribuição-CompartilhaIgual 4.0 Internacional</a>. '

        pages = []
        for (dirpath, dirnames, filenames) in os.walk(htmldir):
            pages.extend(filenames)
            break

        for p in pages:
            fn,ext = os.path.splitext(p)
            if (ext == '.html'):
                print("goodies: affecting "+htmldir+"/"+p)
                #lê a página atual
                f = open(htmldir+"/"+p,'r')
                page = f.read()
                f.close()

                #modifica o __head__
                page = page.replace('</head>',head)

                #modifica o __body__ (top)
                page = page.replace('<body>',body)
                #modifica o __body__ (bottom)
                page = page.replace('</body>',body_end)

                #cria botões de link para o repo/src
                if (fn != 'main'):
                    src_fname = fn
                    if (fn[0:4] == 'cap_'):
                        pos = fn.find('_sec')
                        if (pos != -1):
                            src_fname = fn[0:pos]

                    link_to_src = '<small><a href="https://github.com/phkonzen/notas/blob/master/src/'
                    link_to_src += srcref
                
                    if (src_fname[0:4] == 'cap_'):
                        link_to_src += '/'+src_fname+'/'+src_fname+'.tex'
                    elif (src_fname == 'bib'):
                        link_to_src += '/main.bib'
                    else:
                        link_to_src += '/'+src_fname+'.tex'

                    link_to_src += '" target=_blank> <span class="glyphicon glyphicon-pencil"></span> </a>'
                    link_to_src += '<a href="../contato.html" target="_blank">'
                    link_to_src += ' <span class="glyphicon glyphicon-envelope"></span> </a></small>'

                    page = page.replace('</h1>',link_to_src+'</h1>')
                    page = page.replace('</h2>',link_to_src+'</h2>')

                    # #cria formulário de contato
                    # f = open("contato.html",'r')
                    # tcon = f.read()
                    # f.close()

                    # tcon = tcon.replace('+++fromurl+++',srcref+'/'+p)

                    # f = open(htmldir+'/contato_'+p,'w')
                    # f.write(tcon)
                    # f.close()

                #colapsa as respostas dos exercícios
                paux = page.find('ltx_theorem_resp')
                while (paux != -1):
                    pini = page[paux:0:-1].find('<')
                    pini = paux - pini
                    pter = paux+len('ltx_theorem_resp')+2
                    taux = page[pini:pter]
                    paux = taux.index('id="')+4
                    respid = taux[paux:]
                    paux = respid.index('"')
                    respid = respid[0:paux]
                    page = page.replace(taux, \
                                '<small><button data-toggle="collapse" '+ \
                                'data-target="#'+respid+'">Resp.'+ \
                                '</button></small>'+ \
                                '\n<div id="'+respid+'" class="collapse">\n')
                    paux = page.find('ltx_theorem_resp')
                    
                #modifica o __footer__
                page = page.replace('<div class="ltx_page_logo">',foot)

                #sobrescreve a página com as alterações
                f = open(htmldir+"/"+p,'w')
                f.write(page)
                f.close()

        
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


    
