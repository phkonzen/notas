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
        self.page += '<html lang="pt">\n'
        self.page += '</html>'

    def add_head(self):
        head = '<head>\n'
        
        head += '<title>Notas de aula</title>\n'
        head += '<meta charset="utf-8">\n'
        head += '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        head += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n'
        head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n'
        head += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\n'
        
        head += '</head>\n'

        #add at bottom
        self.page = self.page.replace('</html>',head)
        self.page += '</html>'

    def add_body(self):
        body = '<body>\n'
        body += '<div class="row">\n'
        body += '<div class="col-xs-12 col-xs-offset-0 col-md-8 col-md-offset-2">\n'
        
        #jumbotron
        body += '<div class="jumbotron text-center">\n'
        body += '<h1>Notas de Aula</h1>\n'
        body += '<p>Pedro H A Konzen</p>\n'
        body += '</div>\n'

        #miolo
        body += '<div class="container-fluid">\n'
        body += '<div class="row">\n'

        #notas de aula
        body += '<div class="col-md-6">\n'

        body += '<h3>Notas de aula</h3>\n'
        body += '<ul>\n'        
        #AnaliseMatematica
        body += '<li>Análise Matemática</li>\n'
        body += '<ul class="list-unstyled">\n'
        body += '<li>Versão corrente: '
        body += '<a href="./AnaliseMatematica/main.html">HTML</a>'
        body += ' | '
        body += '<a href="./AnaliseMatematica/main.pdf">PDF</a> '
        body += '</ul>\n'
        #MatematicaNumerica
        body += '<li>Matemática Numérica</li>\n'
        body += '<ul class="list-unstyled">\n'
        body += '<li>Versão corrente: '
        body += '<a href="./MatematicaNumerica/main.html">HTML</a>'
        body += ' | '
        body += '<a href="./MatematicaNumerica/main.pdf">PDF</a> '
        body += '</ul>\n'
        body += '</ul>\n'

        body += '</div> <!-- div class="col-md-6" -->\n'

        body += '<div class="col-md-6">\n'

        body += '<h3>Sobre</h3>\n'
        body += '<p>Neste <i>site</i> disponibilizo minhas notas de aula \n'
        body += 'em formato HTML e PDF. As notas estão predominante escritas \n'
        body += 'em linguagem de marcação \n'
        body += '<a href="https://www.latex-project.org/" target=_blank>LaTeX</a>.</p>\n'
        body += '<p>Buscando fomentar a educação, as notas estão disponíveis \n'
        body += 'sob licença \n'
        body += '<a href="http://creativecommons.org/licenses/by-sa/4.0/deed.pt_BR" target=_blank>CC-BY-SA 4.0</a>. \n'
        body += 'Além disso, você pode acessar os códigos-fonte do material no \n'
        body += 'seguinte repositório GitHub \n'
        body += '<a href="https://github.com/phkonzen/notas">https://github.com/phkonzen/notas</a>.<p>\n'
        body += '<p>Aproveito para agradecer aos(às) estudantes e colegas que \n'
        body += 'de modo assíduo ou esporádico contribuem com sugestões, críticas e correções! :)\n'
        body += '</p>'

        body += '</div><!-- div class="col-md-6" -->\n'

        body += '</div>\n'
        body += '</div>\n'

        body += '</div>\n'
        body += '</div>\n'
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
