#!/usr/bin/python3
'''
index.html

Autor: Pedro H A Konzen - 05/2018
Modificado: 04/2020
'''

import os

class Index:
    
    def __init__(self,odir):
        self.odir = odir
        self.page = ''
        
    def empty_page(self):
        self.page += '<!DOCTYPE html>\n'
        self.page += '<html lang="pt">\n'
        self.page += '</html>'

    def add_head(self):
        head = '<head>\n'
        
        head += '<title>Notas de aula</title>\n'
        head += '<meta charset="utf-8">\n'
        head += '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        head += '<link rel="stylesheet" href="index.css" type="text/css">\n'
        head += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n'
        head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n'
        head += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\n'

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
        #body += '<div class="container">\n'
        body += '<div class="row">\n'
        body += '<div class="col-xs-12 col-xs-offset-0 col-md-8 col-md-offset-2">\n'
        
        #jumbotron
        body += '<div class="extjumbotron">\n'
        body += '<div class="jumbotron text-center">\n'
        body += '<h1>Notas de Aula</h1>\n'
        body += '<p>Pedro H A Konzen</p>\n'
        body += '</div>\n'
        body += '<p>Imagem: <a href="https://www.flickr.com/photos/elisfanclub/2189154850/" target="_blank">Eli Duke</a>.</p>\n'
        body += '</div>\n'

        #miolo
        body += '<div class="container-fluid">\n'
        body += '<div class="row">\n'

        #notas de aula
        body += '<div class="col-md-4">\n'

        body += '<h3>Notas de aula</h3>\n'

        body += '<ul>\n'        

        # #AnaliseMatematicaI
        # body += '<li>Análise Matemática I</li>\n'
        # body += '<ul class="list-unstyled">\n'
        # body += '<li>Versão corrente: '
        # body += '<a href="./AnaliseMatematicaI/main.html">HTML</a>'
        # body += ' | '
        # body += '<a href="./AnaliseMatematicaI/main.pdf">PDF</a></li>'
        # body += '</ul>\n'
        #CalculoI
        body += '<li><strong>Cálculo I</strong></li>\n'
        body += '<ul class="list-unstyled">\n'
        body += '<li>Versão corrente: '
        body += '<a href="./CalculoI/main.html">HTML</a>'
        body += ' | '
        body += '<a href="./CalculoI/main.pdf">PDF</a></li>'
        body += '</ul></br>\n'
        #EDO
        body += '<li><strong>Equações Diferenciais Ordinárias</strong></li>\n'
        body += '<ul class="list-unstyled">\n'
        body += '<li>Versão corrente: '
        body += '<a href="./EDO/main.html">HTML</a>'
        body += ' | '
        body += '<a href="./EDO/main.pdf">PDF</a></li>'
        body += '</ul></br>\n'
        #MatematicaNumerica
        body += '<li><strong>Matemática Numérica</strong></li>\n'
        body += '<ul class="list-unstyled">\n'
        body += '<li>Versão corrente: '
        body += '<a href="./MatematicaNumerica/main.html">HTML</a>'
        body += ' | '
        body += '<a href="./MatematicaNumerica/main.pdf">PDF</a></li>'
        body += '</ul></br>\n'
        
        body += '</ul>\n'

        body += '</div> <!-- div class="col-md-4" -->\n'

        body += '<div class="col-md-4">\n'

        body += '<h3>&nbsp;</h3>\n'

        body += '<ul>\n'        

        #MetodoElementosFinitos
        body += '<li><strong>Método de Elementos Finitos</strong></li>\n'
        body += '<ul class="list-unstyled">\n'
        body += '<li>Versão corrente: '
        body += '<a href="./MetodoElementosFinitos/main.html">HTML</a>'
        body += ' | '
        body += '<a href="./MetodoElementosFinitos/main.pdf">PDF</a></li>'
        body += '</ul></br>\n'
        #Vetores
        body += '<li><strong>Vetores</strong></li>\n'
        body += '<ul class="list-unstyled">\n'
        body += '<li>Versão corrente: '
        body += '<a href="./Vetores/main.html">HTML</a>'
        body += ' | '
        body += '<a href="./Vetores/main.pdf">PDF</a></li>'
        body += '</ul></br>\n'
        #GeometriaAnalitica
        body += '<li><strong>Geometria Analítica</strong></li>\n'
        body += '<ul class="list-unstyled">\n'
        body += '<li>Versão corrente: '
        body += '<a href="./GeometriaAnalitica/main.html">HTML</a>'
        body += ' | '
        body += '<a href="./GeometriaAnalitica/main.pdf">PDF</a></li>'
        body += '</ul></br>\n'
        
        body += '</ul>\n'

        body += '</div> <!-- div class="col-md-3" -->\n'


        #Minicurso
        body += '<div class="col-md-4">\n'
        
        body += '<h3>Minicurso de Cálculo com Python</h3>\n'
        body += '<p><a href="https://mybinder.org/v2/gh/phkonzen/notas/master?filepath=%2Fsrc%2FMiniCalcPy"><img src="https://mybinder.org/badge_logo.svg" alt="Binder" title="" /></a></p>'

        body += '<ul>\n'
        body += '<li>Parte 1 - Funções de uma variável: <a href="MiniCalcPy/1-funcoes.html">HTML</a> | <a href="MiniCalcPy/1-funcoes.ipynb" download>IPYNB</a></li>\n'
        body += '<li>Parte 2 - Limites: <a href="MiniCalcPy/2-limites.html">HTML</a> | <a href="MiniCalcPy/2-limites.ipynb" download>IPYNB</a></li>\n'
        body += '<li>Parte 3 - Derivadas: <a href="MiniCalcPy/3-derivada.html">HTML</a> | <a href="MiniCalcPy/3-derivada.ipynb" download>IPYNB</a></li>\n'
        body += '<li>Parte 4 - Integrais: <a href="MiniCalcPy/4-integracao.html">HTML</a> | <a href="MiniCalcPy/4-integracao.ipynb" download>IPYNB</a></li>\n'
        body += '</ul>\n'

        body += '</div> <!-- div class="col-md-4" -->\n'

        
        body += '</div><!-- div class="row" -->\n'
        body += '</div><!-- div class="container-fluid" -->\n'
        

        body += '<div class="container-fluid">\n'
        body += '<div class="row">\n'

        body += '<div class="col-md-6">\n'

        body += '<h3>Sobre</h3>\n'
        body += '<p>Neste <i>site</i> publico minhas notas de aula \n'
        body += 'em formato HTML e PDF. As notas estão predominante escritas \n'
        body += 'em linguagem de marcação \n'
        body += '<a href="https://www.latex-project.org/" target=_blank>LaTeX</a>.</p>\n'
        body += '<p>As notas estão disponíveis \n'
        body += 'sob licença \n'
        body += '<a href="http://creativecommons.org/licenses/by-sa/4.0/deed.pt_BR" target=_blank>CC-BY-SA 4.0</a>. \n'
        body += 'Além disso, você pode acessar os códigos-fonte do material no \n'
        body += 'seguinte repositório GitHub \n'
        body += '<a href="https://github.com/phkonzen/notas">https://github.com/phkonzen/notas</a>.</p>\n'
        body += '<p>Aproveito para agradecer aos(às) estudantes e colegas que \n'
        body += 'de modo assíduo ou esporádico contribuem com sugestões, críticas e correções! :)\n'
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

        body += '</div>\n'

        #panel footer
        #body += '<div class="container-fluid">\n'
        body += '<div class="panel panel-default">\n'
        body += '<div class="panel-body" style="text-align: right">\n'
        body += 'Repositório GitHub: '
        body += '<a href="https://github.com/phkonzen/notas" target="_blank">https://github.com/phkonzen/notas</a>. Contato '
        body += '<a href="contato.html" target="_blank"><span class="glyphicon glyphicon-envelope"></span></a>\n'
        body += '</div>\n'
        body += '</div>\n'
        #body += '</div>\n'


        body += '</div>\n'
        body += '</div>\n'
        #body += '</div>\n'

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
        os.system('cp index.css '+self.odir+'/')
