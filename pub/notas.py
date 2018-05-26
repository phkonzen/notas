#!/usr/bin/python3


'''
Classe mãe das notas de aula.

Autor: Pedro H A Konzen - 05/2018
'''

import os

class Notas:

    def __init__(self):
        raise ValueError("Você não devia estar aqui!!!")

    def goodies(self,htmldir,nome_notas):
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
        body += '<a class="navbar-brand" href="../index.html">Notas de Aula<br/><small>'+nome_notas+'<small/></a>\n'
        body += '</div>\n\n'

        body += '<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n'
        body += '<ul class="nav navbar-nav">\n'
        body += '<li><a href="https://github.com/phkonzen/notas">Repositório GitHub</a></li>\n'
        body += '<li><a href="main.pdf">Baixar PDF</a></li>\n'
        body += '<li><a href="https://creativecommons.org/licenses/by-sa/4.0/deed.pt_BR">CC-BY-SA 4.0</a></li>\n'
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
            print(ext)
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

                #modifica o __footer__
                page = page.replace('<div class="ltx_page_logo">',foot)

                #sobrescreve a página com as alterações
                f = open(htmldir+"/"+p,'w')
                f.write(page)
                f.close()
            
        

        
