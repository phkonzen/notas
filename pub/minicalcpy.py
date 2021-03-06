#!/usr/bin/python3
'''
Publica as notas de Cálculo I.

notas/src/CalculoI

Autor: Pedro H A Konzen - 03/2019
'''

import os

from notas import *

class MiniCalcPy(Notas):
    
    def __init__(self,srcdir,odir):
        self.srcdir = srcdir
        self.odir = odir
        
    def make_html(self):
        os.chdir(self.srcdir+'/MiniCalcPy')
        os.system('jupyter-nbconvert --to html 1-funcoes.ipynb')
        os.system('jupyter-nbconvert --to html 2-limites.ipynb')
        os.system('jupyter-nbconvert --to html 3-derivada.ipynb')
        os.system('jupyter-nbconvert --to html 4-integracao.ipynb')
        os.chdir('../..')
      
    def build(self):
        #html
        self.make_html()
        self.goodies(self.srcdir+'/MiniCalcPy',\
                         'Minicurso de Cálculo com Python', 'MiniCalcPy')
        os.system('rm -rvf '+self.odir+'/MiniCalcPy')
        os.system('mv '+self.srcdir+'/MiniCalcPy'\
                      +' '+self.odir+'/MiniCalcPy')
        os.system('rm '+self.odir+'/MiniCalcPy/.gitignore')
        os.system('rm -rvf '+self.odir+'/MiniCalcPy/.ipynb*')

        
    def goodies(self,htmldir,titulo_notas,srcref):

        # adiciona goodies.css
        f = open(htmldir+'/goodies.css','w')
        
        text = '.navbar {\n'
        text += 'font-family: Computer Modern Serif;\n'
        text += 'font-size: 1.5em;\n'
        text += '}\n\n'

        text += '.navbar-brand {\n'
        text += 'height: auto;\n'
        text += 'padding: 5px;\n'
        text += 'font-family: Computer Modern Serif;\n'
        text += 'font-size: 1em;\n'
        text += '}\n\n'

        text += '.toast {\n'
        text += 'font-family: Computer Modern Serif;\n'
        text += 'font-size: 1em;\n'
        text += '}\n\n'
        
        f.write(text)
        f.close()
        
        #enxerta no __head__
        head = ''
        
        head += '<meta name="author" content="Pedro H A Konzen"/>\n'
        head += '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n'

        #BootstrapCDN v.4.5
        head += '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">\n'

        # FontAwesome
        head += '<script src="https://kit.fontawesome.com/dfbff2c7ed.js" crossorigin="anonymous"></script>'

        # Goodies CSS
        head += '<link rel="stylesheet" href="goodies.css" type="text/css">\n'

        head += '\n\n'
        head+= '<!-- JavaScript -->\n'
        head += '<!-- jQuery first, then Popper.js, then Bootstrap JS -->\n'
        head += '<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>\n'
        head += '<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>\n'
        head += '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>\n\n'

        head += '<script>'
        head += '$(document).ready(function(){'
        head += '$(".toast").toast();'
        head += '});'
        head += '</script>'


        # Google tracking
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

        # body += '<div class="row">\n'

        body += '<div class=container-fluid>\n'
        body += '<div class=row>\n'
        body += '<div class=col-lg-1>\n'
        body += '</div>'
        body += '<div class=col-lg-10>\n\n'
      
        # Navbar
        body += '\n\n<!-- begin: navbar -->\n'
        body += '<nav class="navbar navbar-expand-md navbar-light bg-light">\n'
        body += '<a class="navbar-brand" href="main.html">Notas de Aula<br/><small>'+titulo_notas+'</small></a>\n'
        body += '<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">\n'
        body += '<span class="navbar-toggler-icon"></span>\n'
        body += '</button>\n'
        body += '<div class="collapse navbar-collapse" id="navbarNav">\n'
        body += '<ul class="navbar-nav">\n'
        body += '<li class="nav-item"><a class="nav-link" href="https://github.com/phkonzen/notas">Repositório GitHub</a></li>\n'
        body += '<li class="nav-item"><a class="nav-link" href="main.pdf">Baixar PDF</a></li>\n'
        body += '<li class="nav=item"><a class="nav-link" href="https://mybinder.org/v2/gh/phkonzen/notas/master?filepath=notas.ipynb" target="_blank">Jupyter NB</a></li>\n'
        body += '<li class="nav-item"><a class="nav-link" href="../index.html">Outras Notas & Infos</a></li>\n'
        body += '</ul>\n'
        body += '</div><!-- /.navbar-collapse -->\n'
        body += '</nav>\n'
        body += '\n\n<!-- end: navbar -->\n\n\n'

       
        #enxerta no __body__ (bottom)
        body_end = ''

        body_end += '<div class="card-footer text-right">\n'
        body_end += '<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Licença Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a><br />O texto acima está sob Licença <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/deed.pt_BR">Creative Commons Atribuição-CompartilhaIgual 4.0 Internacional</a>.  Contato '
        body_end += '<a href="contato.html" target="_blank"><i class="fas fa-envelope"></i></a>\n'
        body_end += '</div> <!-- div class="card-footer text-right" -->\n'


        # botão flutuante fixo 
        body_end += '<div class="toast fade show" style="position: fixed; bottom: 0">'
        body_end += '<div class="toast-header">'
        body_end += '<strong class="mr-auto"><a href="../contato.html" target="_blank"><i class="fas fa-envelope"></i> Erros? Sugestões? </a></strong>'
        body_end += '<button type="button" class="ml-2 mb-1 close" data-dismiss="toast">&times;</button>'
        body_end += '</div>'
        body_end += '<div class="toast-body">'
        body_end += '<a href="../contato.html" target="_blank">Clique aqui para informar erros ou deixar sujestões!</a>'
        body_end += '</div>'
        body_end += '</div>'

        
        body_end += '</div> <!-- div class=col-lg-1 -->\n'
        body_end += '<div class=col-lg-1>\n'
        body_end += '</div>\n'
        body_end += '</div> <!-- div class=row -->\n'
        body_end += '</div> <!-- div class=container-fluid -->\n\n'

        body_end += '</body>\n'

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

                #sobrescreve a página com as alterações
                f = open(htmldir+"/"+p,'w')
                f.write(page)
                f.close()


    # def goodies(self,htmldir,titulo_notas,srcref):
    #     #adiciona goodies.css
    #     f = open(htmldir+'/goodies.css','w')

    #     text = '.navbar {\n'
    #     text += 'font-family: Computer Modern Serif;\n'
    #     text += 'font-size: 1.5em;\n'
    #     text += '}\n\n'

    #     text += '.navbar-brand {\n'
    #     text += 'height: auto;\n'
    #     text += 'padding: 5px;\n'
    #     text += 'font-family: Computer Modern Serif;\n'
    #     text += '}\n\n'
       
    #     f.write(text)
    #     f.close()
        
    #     #enxerta no __head__
    #     head = ''
        
    #     head += '<meta name="author" content="Pedro H A Konzen"/>\n'
    #     head += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n'
    #     head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n'
    #     head += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\n'
    #     head += '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    #     head += '<link rel="stylesheet" href="goodies.css" type="text/css">\n'

    #     #google tracking
    #     head += '\n<!-- Global site tag (gtag.js) - Google Analytics -->\n'
    #     head += '<script async src="https://www.googletagmanager.com/gtag/js?id=UA-17226092-2"></script>\n'
    #     head += '<script>\n'
    #     head += 'window.dataLayer = window.dataLayer || [];\n'
    #     head += 'function gtag(){dataLayer.push(arguments);}\n'
    #     head += 'gtag("js", new Date());\n'
    #     head += '\ngtag("config", "UA-17226092-2")\n';
    #     head += '</script>\n'

        
    #     head += '</head>\n'

    #     #enxerta no __body__ (top)
    #     body = '<body>\n\n'

    #     body += '<div class="row">\n'
    #     body += '<div class="col-xs-12 col-xs-offset-0 col-md-8 col-md-offset-1">\n'


    #     body += '\n\n<!-- begin: navbar -->\n'
    #     body += '<nav class="navbar navbar-default">\n'
    #     body += '<div class="container-fluid">\n'
    #     body += '<div class="navbar-header">\n'
    #     body += '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\n'
    #     body += '<span class="sr-only">Toggle navigation</span>\n'
    #     body += '<span class="icon-bar"></span>\n'
    #     body += '<span class="icon-bar"></span>\n'
    #     body += '<span class="icon-bar"></span>\n'
    #     body += '</button>\n'
    #     body += '<a class="navbar-brand" href="../index.html">Notas de Aula<br/><small>'+titulo_notas+'<small/></a>\n'
    #     body += '</div>\n\n'

    #     body += '<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n'
    #     body += '<ul class="nav navbar-nav">\n'
    #     body += '<li><a href="https://github.com/phkonzen/notas">Repositório GitHub</a></li>\n'
    #     body += '<li><a href="https://mybinder.org/v2/gh/phkonzen/notas/master?filepath=%2Fsrc%2FMiniCalcPy%2Fminicalcpy.ipynb" target="_blank">Jupyter NB</a></li>\n'
    #     # body += '<li><a href="https://creativecommons.org/licenses/by-sa/4.0/deed.pt_BR">CC-BY-SA 4.0</a></li>\n'
    #     body += '<li><a href="../index.html">Outras Notas & Infos</a></li>\n'
    #     body += '</ul>\n'
    #     body += '</div><!-- /.navbar-collapse -->\n'
    #     body += '</div><!-- /.container-fluid -->\n'
    #     body += '</nav>\n'
    #     body += '\n\n<!-- end: navbar -->\n\n\n'

    #     #enxerta no __body__ (bottom)
    #     body_end = ''

    #     body_end += '<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Licença Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a><p style="fontsize=6pt">O texto acima está sob Licença <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/deed.pt_BR">Creative Commons Atribuição-CompartilhaIgual 4.0 Internacional</a>.</p> '

    #     body_end += '</div><!-- div class="row" -->\n'
    #     body_end += '</div><!-- div class="col-xs-12 col-xs-offset-0 col-md-8 col-md-offset-2 -->\n'

    #     body_end += '</body>'

    #     pages = []
    #     for (dirpath, dirnames, filenames) in os.walk(htmldir):
    #         pages.extend(filenames)
    #         break

    #     for p in pages:
    #         fn,ext = os.path.splitext(p)
    #         if (ext == '.html'):
    #             print("goodies: affecting "+htmldir+"/"+p)
    #             #lê a página atual
    #             f = open(htmldir+"/"+p,'r')
    #             page = f.read()
    #             f.close()

    #             #modifica o __head__
    #             page = page.replace('</head>',head)

    #             #modifica o __body__ (top)
    #             page = page.replace('<body>',body)
    #             #modifica o __body__ (bottom)
    #             page = page.replace('</body>',body_end)                    

    #             #sobrescreve a página com as alterações
    #             f = open(htmldir+"/"+p,'w')
    #             f.write(page)
    #             f.close()
