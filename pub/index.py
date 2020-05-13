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
        head += '<link rel="stylesheet" href="index.css" type="text/css">\n'

        # # BootstrapCDN v3.3
        # head += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n'
        # head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n'
        # head += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\n'

        #BootstrapCDN v.4.5
        head += '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk"x crossorigin="anonymous">\n'

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
        
        head += '</head>\n'

        #add at bottom
        self.page = self.page.replace('</html>',head)
        self.page += '</html>'

    def add_body(self):
        body = '<body>\n'
        
        body += '<div class=container-fluid>\n'
        body += '<div class=row>\n'
        body += '<div class=col-lg-1>\n'
        body += '</div>'
        body += '<div class=col-lg-10>\n\n'

        # #jumbotron
        # body += '<div class="extjumbotron">\n'
        # body += '<div class="jumbotron text-center">\n'
        # body += '<h1>Notas de Aula</h1>\n'
        # body += '<p>Pedro H A Konzen</p>\n'
        # body += '</div> <!-- div class="jumbotron text-center" -->\n'
        # body += '<p>Imagem: <a href="https://www.flickr.com/photos/elisfanclub/2189154850/" target="_blank">Eli Duke</a>.</p>\n'
        # body += '</div> <!-- div class=extjumbotron -->\n\n'

        #jumbotron
        body += '<div class="myjumbotron">\n'
        body += '<div class="jumbotron text-center">\n'
        body += '<h1 class="display-4">Notas de Aula</h1>\n'
        body += '<hr class="my-4">'
        body += '<p class="lead">Pedro H A Konzen</p>\n'
        body += '</div> <!-- div class="jumbotron text-center" -->\n'
        body += '<p style="text-align:right">Imagem: <a href="https://www.flickr.com/photos/elisfanclub/2189154850/" target="_blank">Eli Duke</a>.</p>\n'
        body += '</div> <!-- class="myjumbotron" -->\n'

        
        
        #miolo

        body += '<h3>Notas de aula</h3>\n\n'


        body += '<div class=row>\n'
        # card: notas de aula de Cálculo I
        body += '<div class="col-lg-3 col-md-4 col-sm-6">'
        body += '<!-- card: notas de aula de Cálculo I -->\n'
        body += '<div class="card border-primary mb-3" style="max-width: 20rem;">\n'
        body += '<div class="card-header">Notas de aula</div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Cálculo I</h5>\n'
        body += '<p class="card-text" style="color: gray">Cálculo diferencial e integral de funções de uma variável real</p>\n'
        body += '<a href="./CalculoI/main.html" class="btn btn-primary stretched-link">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: notas de aula de EDO
        body += '<div class="col-lg-3 col-md-4 col-sm-6">'
        body += '<!-- card: notas de aula de EDO -->\n'
        body += '<div class="card border-primary mb-3" style="max-width: 20rem;">\n'
        body += '<div class="card-header">Notas de aula</div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Equações diferencias ordinárias</h5>\n'
        body += '<p class="card-text" style="color: gray">Introdução a equações diferenciais ordinárias</p>\n'
        body += '<a href="./EDO/main.html" class="btn btn-primary stretched-link">\n'
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
        body += '<a href="./GeometriaAnalitica/main.html" class="btn btn-primary stretched-link">\n'
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
        body += '<a href="./MatematicaNumerica/main.html" class="btn btn-primary stretched-link">\n'
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
        body += '<a href="./MetodoElementosFinitos/main.html" class="btn btn-primary stretched-link">\n'
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
        body += '<a href="./Vetores/main.html" class="btn btn-primary stretched-link">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        body += '</div> <!-- div class=row-->\n\n'

        body += '<h3>Minicurso</h3>\n\n'

        
        # card: Mini Cálculo com python
        body += '<!-- card: Mini Cálculo com python -->\n'
        body += '<div class="card border-primary mb-3" style="max-width: 25rem;">\n'
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

     
        body += '<div class="row">\n'

        body += '<div class="col-md-6">\n'

        body += '<h3>Sobre</h3>\n'
        body += '<p>Neste <i>site</i> publico minhas notas de aula. \n'
        body += 'O matrial está escrito predominante em linguagem de marcação \n'
        body += '<a href="https://www.latex-project.org/" target=_blank>LaTeX</a>. \n'
        body += 'Disponíveis sob licença \n'
        body += '<a href="http://creativecommons.org/licenses/by-sa/4.0/deed.pt_BR" target=_blank>CC-BY-SA 4.0</a>, \n'
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
        body += '<li><a href="http://lattes.cnpq.br/2565213716047382" target="_blank">Currículo Lattes</a></li>\n'
        body += '<li><a href="http://professor.ufrgs.br/pedro/" target="_blank">Página de professor na UFRGS</a></li>\n'
        body += '</ul>\n'

        body += '<h3>Ligações recomendadas</h3>\n'
        body += '<ul>\n'
        body += '<li><a href="https://archive.org/" target="_blank">Internet Archive</a>: biblioteca de milhões de livros, filmes, <i>softwares</i>, música, <i>websites</i> e mais</li>\n'
        body += '<li><a href="https://www.geogebra.org/" target="_blank">Geogebra</a>: aplicativos abertos de matemática</li>\n'
        body += '<li><a href="https://www.ufrgs.br/reamat" target="_blank">REAMAT</a>: projeto de recursos educacionais abertos de matemática</li>\n'
        body += '</ul>\n'

        body += '</div><!-- div class="col-md-6" -->\n'

        body += '</div><!-- div class="row" -->\n'

        # body += '</div>\n'

        # #panel footer
        # #body += '<div class="container-fluid">\n'
        # body += '<div class="panel panel-default">\n'
        # body += '<div class="panel-body" style="text-align: right">\n'
        # body += 'Repositório GitHub: '
        # body += '<a href="https://github.com/phkonzen/notas" target="_blank">https://github.com/phkonzen/notas</a>. Contato: '
        # body += '<a href="contato.html" target="_blank"><span class="glyphicon glyphicon-envelope"></span></a>\n'
        # body += '</div>\n'
        # body += '</div>\n'
        # #body += '</div>\n'

        body += '<div class="card-footer text-right">\n'
        body += 'Repositório GitHub: '
        body += '<a href="https://github.com/phkonzen/notas" target="_blank">https://github.com/phkonzen/notas</a>. Contato '
        body += '<a href="contato.html" target="_blank"><i class="fas fa-envelope"></i></a>\n'
        body += '</div> <!-- div class="card-footer text-right" -->\n'

        # body += '</div> <!-- div class="container-fluid" -->\n'

        body += '</div> <!-- div class=col-lg-10 -->\n'
        body += '<div class=col-lg-1>\n'
        body += '</div>\n'
        body += '</div> <!-- div class=container-fluid -->\n\n'


        body += '\n\n'
        body += '<!-- JavaScript -->\n'
        body += '<!-- jQuery first, then Popper.js, then Bootstrap JS -->\n'
        body += '<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>\n'
        body += '<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>\n'
        body += '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>\n'

        
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
