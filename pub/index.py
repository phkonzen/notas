#!/usr/bin/python3
'''
index.html

Autor: Pedro H A Konzen - 05/2018
Modificado: 05/2020
'''

import os

class Index:
    
    def __init__(self,odir):
        self.odir = odir
        self.page = ''
        
    def empty_page(self):
        self.page += '<!doctype html>\n'
        self.page += '<html lang="pt">\n'
        self.page += '</html>'

    def add_head(self):
        head = '<head>\n'
        
        head += '<meta charset="utf-8">\n'
        head += '<title>Notas de aula</title>\n'
        head += '<meta name="author" content="Pedro H A Konzen"/>\n'
        head += '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n'
        head += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">\n'
        head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>\n'
        head += '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>\n'
        head += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>\n'

        # FontAwesome
        head += '<script src="https://kit.fontawesome.com/dfbff2c7ed.js" crossorigin="anonymous"></script>'
        
        #google tracking
        head += '\n<!-- Global site tag (gtag.js) - Google Analytics -->\n'
        head += '<script async src="https://www.googletagmanager.com/gtag/js?id=UA-17226092-2"></script>\n'
        head += '<script>\n'
        head += 'window.dataLayer = window.dataLayer || [];\n'
        head += 'function gtag(){dataLayer.push(arguments);}\n'
        head += 'gtag("js", new Date());\n'
        head += '\ngtag("config", "UA-17226092-2")\n';
        head += '</script>\n'

        head += '<!-- Computer Modern Serif-->'
        head += '<link rel="stylesheet" href="fonts/cmun-serif.css"></link>'
        head += '<link rel="stylesheet" href="index.css" type="text/css">\n'

        head += '<script>\n'
        head += '$(document).ready(function () {\n'
        head += '$("#colabAlert").hide();\n'
        head += '$("#generalAlert").hide();\n'
        head += 'if (document.referrer.lastIndexOf("://phkonzen.github.io/notas/") == -1) {\n'
        head += '$("#generalAlert").fadeIn(100);\n'
        head += '$("#colabAlert").delay(3000).fadeIn(100);\n'
        head += '}\n'
        head += '});\n'    
        head += '</script>\n\n'
        
        head += '</head>\n'

        #add at bottom
        self.page = self.page.replace('</html>',head)
        self.page += '</html>'

    def add_body(self):
        body = '<body>\n'
        
        body += '<div class="container-fluid">\n'
        body += '<div class="row">\n'
        body += '<div class="col-lg-1">\n'
        body += '</div>'
        body += '<div class="col-lg-10">\n\n'

        # Navbar
        body += '\n\n<!-- begin: navbar -->\n'
        body += '<nav class="navbar navbar-expand-md navbar-light bg-light mb-1">\n'
        body += '<a class="navbar-brand" href="main.html">Notas de Aula<br/><small>Início</small></a>\n'
        body += '<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">\n'
        body += '<span class="navbar-toggler-icon"></span>\n'
        body += '</button>\n'
        body += '<div class="collapse navbar-collapse" id="navbarNav">\n'
        body += '<ul class="navbar-nav">\n'
        body += '<li class="nav-item active"><a class="nav-link" href="index.html"><i class="fas fa-home"></i> Início</a></li>\n'
        body += '<li class="nav=item"><a class="nav-link" href="https://mybinder.org/v2/gh/phkonzen/notas/master?filepath=notas.ipynb">Jupyter NB</a></li>\n'
        body += '<li class="nav-item dropdown">\n'
        body += '<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n'
        body += 'Contato\n'
        body += '</a>\n'
        body += '<div class="dropdown-menu" aria-labelledby="navbarDropdown">\n'
        body += '<a class="dropdown-item" href="./contato.html"><i class="fas fa-envelope"></i> Mensagem</a>\n'
        body += '<a class="dropdown-item" href="https://www.instagram.com/notas.pedrok/"><i class="fab fa-instagram"></i> notas.pedrok</a>\n'
        body += '</div><!-- div class="dropdown-menu" aria-labelledby="navbarDropdown" -->\n'
        body += '</li> <!-- li class="nav-item dropdown" -->\n'
        body += '<li class="nav-item"><a class="nav-link" href="https://github.com/phkonzen/notas"><i class="fa fa-github" aria-hidden="true"></i> Repo</a></li>\n'
        body += '<li class="nav-item"><a class="nav-link" href="./politica.html">Política de dados</a></li>\n'
        body += '</ul>\n'
        body += '</div><!-- /.navbar-collapse -->\n'
        body += '</nav>\n'
        body += '\n\n<!-- end: navbar -->\n\n\n'


        # jumbotron
        body += '<div class="myjumbotron">\n'
        body += '<div class="jumbotron text-center">\n'
        # body += '<h1 class="display-4 text-left"><i class="fas fa-fist-raised"></i></h1>\n'
        body += '<div class="row">'
        body += '<div class="col-lg-3 col-md-2">'
        body += '</div>'
        body += '<div class="col-lg-6 col-md-8 ">'
        body += '<h1 class="display-4 bg-white text-dark mb-0" style="opacity:75%;">Notas de Aula</h1>\n'
        # body += '<hr class="my-4">'
        body += '<p class="lead bg-white text-dark mt-0" style="opacity:75%;">Pedro H A Konzen</p>\n'
        body += '</div>'
        body += '</div>'
        body += '</div> <!-- div class="jumbotron text-center" -->\n'
        body += '<p class="mb-0" style="text-align:right"><small>Imagem: <a href="https://flic.kr/p/4krYcm">Eli Duke</a>.</small></p>\n'
        body += '</div> <!-- class="myjumbotron" -->\n'

        
        
        #miolo

        # Área de anúncios
        #body += '<p></p>'
        body += '<div id="demo" class="carousel slide" data-ride="carousel">'
        body += '<!-- Indicators -->'
        body += '<ul class="carousel-indicators">'
        body += '<li data-target="#demo" data-slide-to="0"></li>'
        # body += '<li data-target="#demo" data-slide-to="1"></li>'
        # body += '<li data-target="#demo" data-slide-to="2"></li>'
        body += '</ul>'
        
        body += '<!-- The slideshow -->'
        body += '<div class="carousel-inner">\n'
        
        body += '<div class="carousel-item active">\n'
        body += '<div>\n'
        body += '<div class="spinner-grow spinner-grow-sm text-primary mb-1" role="status"></div>\n'
        body += '<a href="http://www.cnmac.org.br">XL CNMAC 13 - 17/09/21</a>\n'
        body += '</div>\n'
        body += '</div>\n\n'


        body += '<div class="carousel-item">\n'
        body += '<div>\n'
        body += '<div class="spinner-grow spinner-grow-sm text-primary mb-1" role="status"></div>\n'
        body += '<a href="http://www.ufrgs.br/ppgmap/selecao/editais-de-selecao-doutorado">PPGMAp-UFRGS: Processo Seletivo Doutorado 2021</a>\n'
        body += '</div>\n'        
        body += '</div>\n\n'

        body += '<div class="carousel-item">\n'
        body += '<div>\n'
        body += '<div class="spinner-grow spinner-grow-sm text-primary mb-1" role="status"></div>\n'
        body += '<a href="https://semanacademicamat.wixsite.com/home">XV SEMANACA - UFRGS: 07-11/06/2021</a>\n'
        body += '</div>\n'
        body += '</div>'


        body += '</div>'
  
        body += '</div>'

        body += '<h3 class="mt-1">Notas de aula</h3>\n\n'


        body += '<div class=row>\n'
        # card: notas de aula de Cálculo I
        body += '<div class="col-lg-3 col-md-4 col-sm-6">'
        body += '<!-- card: notas de aula de Cálculo I -->\n'
        body += '<div class="card border-primary mb-3" style="max-width: 20rem;">\n'
        body += '<div class="card-header">Notas de aula</div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Cálculo I</h5>\n'
        body += '<p class="card-text" style="color: gray">Cálculo diferencial e integral de funções de uma variável real</p>\n'
        body += '<a href="./CalculoI/main.html" class="btn btn-primary float-right">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: notas de aula de EaD
        body += '<div class="col-lg-3 col-md-4 col-sm-6">'
        body += '<!-- card: notas de aula de EaD -->\n'
        body += '<div class="card border-success mb-3" style="max-width: 20rem;">\n'
        body += '<div class="card-header">Notas de aula</div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Equações a diferenças</h5>\n'
        body += '<p class="card-text" style="color: gray">Introdução a equações a diferenças</p>\n'
        body += '<a href="./EaD/main.html" class="btn btn-success float-right">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: notas de aula de EDO
        body += '<div class="col-lg-3 col-md-4 col-sm-6">'
        body += '<!-- card: notas de aula de EDO -->\n'
        body += '<div class="card border-success mb-3" style="max-width: 20rem;">\n'
        body += '<div class="card-header">Notas de aula</div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Equações diferencias ordinárias</h5>\n'
        body += '<p class="card-text" style="color: gray">Introdução a equações diferenciais ordinárias</p>\n'
        body += '<a href="./EDO/main.html" class="btn btn-success float-right">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: Geometria analítica
        body += '<div class="col-lg-3 col-md-4 col-sm-6">'
        body += '<!-- card: Geometria analítica -->\n'
        body += '<div class="card border-primary mb-3" style="max-width: 20rem;">\n'
        body += '<div class="card-header">Notas de aula</div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Geometria analítica</h5>\n'
        body += '<p class="card-text" style="color: gray">Introdução à geometria analítica</p>\n'
        body += '<a href="./GeometriaAnalitica/main.html" class="btn btn-primary float-right">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: notas de aula de Matemática numérica
        body += '<div class="col-lg-3 col-md-4 col-sm-6">'
        body += '<!-- card: notas de aula de Matemática numérica -->\n'
        body += '<div class="card border-primary mb-3" style="max-width: 20rem;">\n'
        body += '<div class="card-header">Notas de aula</div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Matemática numérica</h5>\n'
        body += '<p class="card-text" style="color: gray">Métodos e técnicas de cálculo numérico</p>\n'
        body += '<a href="./MatematicaNumerica/main.html" class="btn btn-primary float-right">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: notas de aula de Matemática Numérica Paralela
        body += '<div class="col-lg-3 col-md-4 col-sm-6">'
        body += '<!-- card: notas de aula de Matemática numérica paralela -->\n'
        body += '<div class="card border-warning mb-3" style="max-width: 20rem;">\n'
        body += '<div class="card-header">Notas de aula</div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Matemática numérica paralela</h5>\n'
        body += '<p class="card-text" style="color: gray">Introdução à computação paralela aplicada a métodos numéricos</p>\n'
        body += '<a href="./MatematicaNumericaParalela/main.html" class="btn btn-warning float-right">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: Método de elementos finitos
        body += '<div class="col-lg-3 col-md-4 col-sm-6">'
        body += '<!-- card: Método de elementos finitos -->\n'
        body += '<div class="card border-primary mb-3" style="max-width: 20rem;">\n'
        body += '<div class="card-header">Notas de aula</div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Método de elementos finitos</h5>\n'
        body += '<p class="card-text" style="color: gray">Introdução ao método de elementos finitos</p>\n'
        body += '<a href="./MetodoElementosFinitos/main.html" class="btn btn-primary float-right">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: Vetores
        body += '<div class="col-lg-3 col-md-4 col-sm-6">'
        body += '<!-- card: Vetores -->\n'
        body += '<div class="card border-primary mb-3" style="max-width: 20rem;">\n'
        body += '<div class="card-header">Notas de aula</div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Vetores</h5>\n'
        body += '<p class="card-text" style="color: gray">Vetores no espaço euclidiano tridimensional</p>\n'
        body += '<a href="./Vetores/main.html" class="btn btn-primary float-right">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        body += '</div> <!-- div class=row-->\n\n'

        
        body += '<div class="row">\n'
        body += '<div class="col-md-6">\n'

        body += '<h3>Minicurso</h3>\n\n'

        
        # card: Mini Cálculo com python
        body += '<!-- card: Mini Cálculo com python -->\n'
        body += '<div class="card border-primary mb-3" style="max-width: 24rem;">\n'
        body += '<div class="card-header">Minicurso</div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Cálculo com python</h5>\n'
        body += '<p><a href="https://mybinder.org/v2/gh/phkonzen/notas/master?filepath=%2Fsrc%2FMiniCalcPy"><img src="https://mybinder.org/badge_logo.svg" alt="Binder" title="" /></a></p>'

        body += '<ul>\n'
        body += '<li><a href="MiniCalcPy/1-funcoes.html">Parte 1 - Funções de uma variável</a></li>\n'
        body += '<li><a href="MiniCalcPy/2-limites.html">Parte 2 - Limites</a></li>\n'
        body += '<li><a href="MiniCalcPy/3-derivada.html">Parte 3 - Derivadas</a></li>\n'
        body += '<li><a href="MiniCalcPy/4-integracao.html">Parte 4 - Integrais</a></li>\n'
        body += '</ul>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        body += '</div><!-- div class="col-md-6" -->\n'

        body += '<div class="col-md-6">\n'

        body += '<h3>Vídeos & áudios</h3>'

        # card: Internet Archive
        body += '<!-- card: Internet Archive -->\n'
        body += '<div class="card border-primary mb-3" style="max-width: 20rem;">\n'
        body += '<div class="card-header">Vídeos & áudios</div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Internet Archive</h5>\n'
        body += '<p class="card-text" style="color: gray">Coleção de vídeos e áudios no archive.org.</p>\n'
        body += '<a href="https://archive.org/details/notas-de-aula" class="btn btn-primary float-right">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n\n'
        
        
        body += '</div><!-- div class="col-md-6" -->\n'
        
        body += '</div><!-- div class="row" -->\n'
    
        body += '<div class="row">\n'

        body += '<div class="col-md-6">\n'

        body += '<h3>Sobre</h3>\n'
        body += '<p>Neste <i>site</i> publico minhas notas de aula. \n'
        body += 'O material está escrito predominante em linguagem de marcação \n'
        body += '<a href="https://www.latex-project.org/">LaTeX</a>. \n'
        body += 'Disponíveis sob licença \n'
        body += '<a href="http://creativecommons.org/licenses/by-sa/4.0/deed.pt_BR">CC-BY-SA 4.0</a>, \n'
        body += 'os códigos-fonte podem ser obtidos no \n'
        body += 'repositório GitHub \n'
        body += '<a href="https://github.com/phkonzen/notas">https://github.com/phkonzen/notas</a>.</p>\n'
        body += '<p>Aproveito para agradecer a todos e todas que de forma assídua ou esporádica \n'
        body += 'contribuem com correções, sugestões e críticas! \n'
        body += '<i class="far fa-smile"></i>'
        body += '</p>'

        body += '</div><!-- div class="col-md-6" -->\n'

        body += '<div class="col-md-6">\n'

        body += '<h3>Sobre mim?</h3>\n'
        body += '<ul>\n'
        body += '<li><a href="http://lattes.cnpq.br/2565213716047382">Currículo Lattes</a></li>\n'
        body += '<li><a href="http://professor.ufrgs.br/pedro/">Página de professor na UFRGS</a></li>\n'
        body += '</ul>\n'

        body += '<h3>Ligações recomendadas</h3>\n'
        body += '<ul>\n'
        body += '<li><a href="https://archive.org/">Internet Archive</a>: biblioteca de milhões de livros, filmes, <i>softwares</i>, música, <i>websites</i> e mais</li>\n'
        body += '<li><a href="https://www.geogebra.org/">Geogebra</a>: aplicativos abertos de matemática</li>\n'
        body += '<li><a href="https://www.ufrgs.br/reamat">REAMAT</a>: projeto de recursos educacionais abertos de matemática</li>\n'
        body += '</ul>\n'

        body += '</div><!-- div class="col-md-6" -->\n'

        body += '</div><!-- div class="row" -->\n'

        # rodapé (id=rodape)
        f = open('rodape.html','r')
        body += f.read()
        f.close()

        # colab alert (id=colabAlert)
        f = open('colab_alert.html','r')
        body += f.read()
        f.close()

        # general alert
        f = open('general_alert.html','r')
        body += f.read()
        f.close()

        # body += '</div> <!-- div class="container-fluid" -->\n'

        body += '</div> <!-- div class=col-lg-10 -->\n'
        body += '<div class=col-lg-1>\n'
        body += '</div>\n'
        body += '</div><!-- div row -->\n'
        body += '</div> <!-- div class=container-fluid -->\n\n'


        body += '\n\n'


        body += '</body>\n'


        #add at bottom
        self.page = self.page.replace('</html>',body)
        self.page += '</html>'

    def build(self):
        self.empty_page()
        self.add_head()
        self.add_body()
        f = open(self.odir + '/index.html','w')
        f.write(self.page)
        f.close()

        #put jumbotron image and index.css
        os.system('cp jumbotron.jpg '+self.odir+'/')
        os.system('cp jumbotron2.jpg '+self.odir+'/')
        os.system('cp index.css '+self.odir+'/')
