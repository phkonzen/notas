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
        super().__init__()
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
        text = 'body {\n'
        text += 'font-family: "Computer Modern Serif", serif;\n'
        # text += 'font-size: 110%;\n'
        text += '}\n\n'
        
        text += '.navbar-brand {\n'
        text += 'height: auto;\n'
        text += 'padding: 5px;\n'
        text += 'font-size: 1.75em;\n'
        text += '}\n\n'

        
        f.write(text)
        f.close()

        # # adiciona goodies.css
        # f = open(htmldir+'/goodies.css','w')
        
        # text = '.navbar {\n'
        # text += 'font-family: Computer Modern Serif;\n'
        # text += 'font-size: 1.5em;\n'
        # text += '}\n\n'

        # text += '.navbar-brand {\n'
        # text += 'height: auto;\n'
        # text += 'padding: 5px;\n'
        # text += 'font-family: Computer Modern Serif;\n'
        # text += 'font-size: 1em;\n'
        # text += '}\n\n'

        # text += '.toast {\n'
        # text += 'font-family: Computer Modern Serif;\n'
        # text += 'font-size: 1em;\n'
        # text += '}\n\n'
        
        # f.write(text)
        # f.close()
        
        #enxerta no __head__
        head = ''
        
        head += '<meta name="author" content="Pedro H A Konzen"/>\n'
        head += '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n'

        head += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">\n'
        head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>\n'
        head += '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>\n'
        head += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>\n'

        # FontAwesome
        head += '<script src="https://kit.fontawesome.com/dfbff2c7ed.js" crossorigin="anonymous"></script>'

        # Goodies CSS
        head += '<!-- Computer Modern Serif-->'
        head += '<link rel="stylesheet" href="fonts/cmun-serif.css"></link>'
        head += '<link rel="stylesheet" href="goodies.css" type="text/css">\n'
        
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

        head += '<script>\n'
        head += '$(document).ready(function () {\n'
        head += '$("#colabAlert").hide();\n'
        head += '$("#generalAlert").hide();\n'
        head += 'if (document.referrer.lastIndexOf("://phkonzen.github.io/notas/") == -1) {\n'
        head += '$("#generalAlert").fadeIn(100);\n'
        head += '}\n'
        head += '$("#colabAlert").delay(3000).fadeIn(100);\n'
        head += '});\n'    
        head += '</script>\n\n'
        
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
        body += '<div class="collapse navbar-collapse" id="navbarNav" style="font-size:1.75em;">\n'
        body += '<ul class="navbar-nav">\n'
        body += '<li class="nav-item"><a class="nav-link" href="../index.html"><i class="fas fa-home"></i> Início</a></li>\n'
        body += '<li class="nav=item"><a class="nav-link" href="https://mybinder.org/v2/gh/phkonzen/notas/master?filepath=notas.ipynb">Jupyter NB</a></li>\n'
        body += '<li class="nav-item dropdown">\n'
        body += '<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n'
        body += 'Contato\n'
        body += '</a>\n'
        body += '<div class="dropdown-menu" aria-labelledby="navbarDropdown"  style="font-size:1em;">\n'
        body += '<a class="dropdown-item" href="../contato.html"><i class="fas fa-envelope"></i> Mensagem</a>\n'
        body += '<a class="dropdown-item" href="https://www.instagram.com/notas.pedrok/"><i class="fab fa-instagram"></i> notas.pedrok</a>\n'
        body += '</div><!-- div class="dropdown-menu" aria-labelledby="navbarDropdown" -->\n'
        body += '</li> <!-- li class="nav-item dropdown" -->\n'
        body += '<li class="nav-item"><a class="nav-link" href="https://github.com/phkonzen/notas"><i class="fa fa-github" aria-hidden="true"></i> Repo</a></li>\n'
        body += '<li class="nav-item"><a class="nav-link active" href="../infos.html#colabore"><i class="fa-solid fa-heart" style="color:red;"></i> Colabore</a></li>'
        body += '<li class="nav-item"><a class="nav-link" href="../infos.html#politica">Política de dados</a></li>'
        body += '</ul>\n'
        body += '</div><!-- /.navbar-collapse -->\n'
        body += '</nav>\n'
        body += '\n\n<!-- end: navbar -->\n\n\n'

       
        #enxerta no __body__ (bottom)
        body_end = ''

        body_end += '<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/" style="font-size:1.5em;"><img alt="Licença Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a><br />O texto acima está sob Licença <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/deed.pt_BR">Creative Commons Atribuição-CompartilhaIgual 4.0 Internacional</a>.'

        # rodapé (id=rodape)
        f = open('rodape.html','r')
        rp = f.read()
        f.close()
        rp = rp.replace('style=""','style="font-size:1.75em;"')
        body_end += rp.replace('./contato.html','../contato.html')


        # colab alert
        f = open('colab_alert.html','r')
        ga = f.read()
        f.close()
        ga = ga.replace('style=""','style="font-size:1.75em;"')
        body_end += ga.replace('./contato.html','../contato.html')


        # general alert
        f = open('general_alert.html','r')
        ga = f.read()
        f.close()
        ga = ga.replace('style="','style="font-size:1.75em;')
        body_end += ga.replace('./politica.html','../politica.html')

        
        # # botão flutuante fixo 
        # body_end += '<div class="toast fade show" style="position: fixed; bottom: 0">'
        # body_end += '<div class="toast-header">'
        # body_end += '<strong class="mr-auto"><a href="../contato.html" target="_blank"><i class="fas fa-envelope"></i> Erros? Sugestões? </a></strong>'
        # body_end += '<button type="button" class="ml-2 mb-1 close" data-dismiss="toast">&times;</button>'
        # body_end += '</div>'
        # body_end += '<div class="toast-body">'
        # body_end += '<a href="../contato.html" target="_blank">Clique aqui para informar erros ou deixar sujestões!</a>'
        # body_end += '</div>'
        # body_end += '</div>'

        
        body_end += '</div> <!-- div class=col-lg-1 -->\n'
        body_end += '<div class=col-lg-1>\n'
        body_end += '</div>\n'
        body_end += '</div> <!-- div class=row -->\n'
        body_end += '</div> <!-- div class=container-fluid -->\n\n'

        body_end += '</body>\n'

        #enxerta no __footer__
        foot = '<div class="ltx_page_logo">\n'
        foot += '<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/" style="font-size:1.75em;"><img alt="Licença Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a><br />O texto acima está sob Licença <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/deed.pt_BR">Creative Commons Atribuição-CompartilhaIgual 4.0 Internacional</a>.'

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
                page = page.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>',"")
                page = page.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>',"")
                page = page.replace('</head>',head)

                #modifica o __body__ (top)
                page = page.replace('<body>',body)
                #modifica o __body__ (bottom)
                page = page.replace('</body>',body_end)

                #sobrescreve a página com as alterações
                f = open(htmldir+"/"+p,'w')
                f.write(page)
                f.close()

