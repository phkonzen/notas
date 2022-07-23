#!/usr/bin/python3
'''
politica.html

Autor: Pedro H A Konzen - 05/2021
'''

import os

class Politica:
    
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
        head += '<title>Notas de aula - Política de Uso de Dados</title>\n'
        head += '<meta name="author" content="Pedro H A Konzen"/>\n'
        head += '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n'

        head += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">\n'
        head += '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>\n'
        head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>\n'
        
        # head += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">\n'
        # head += '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>\n'
        # head += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>\n'

        # FontAwesome
        # head += '<script src="https://kit.fontawesome.com/dfbff2c7ed.js" crossorigin="anonymous"></script>'
        head += '<link href="./fontawesome/css/all.min.css" rel="stylesheet">'
        # head += '<link href="./fontawesome/css/brands.css" rel="stylesheet">'
        # head += '<link href="./fontawesome/css/solid.css" rel="stylesheet">'
        
        #google tracking
        f = open('gtag.js','r')
        head += f.read()
        f.close()
        # head += '\n<!-- Global site tag (gtag.js) - Google Analytics -->\n'
        # head += '<script async src="https://www.googletagmanager.com/gtag/js?id=UA-17226092-2"></script>\n'
        # head += '<script>\n'
        # head += 'window.dataLayer = window.dataLayer || [];\n'
        # head += 'function gtag(){dataLayer.push(arguments);}\n'
        # head += 'gtag("js", new Date());\n'
        # head += '\ngtag("config", "UA-17226092-2")\n';
        # head += '</script>\n'

        head += '<!-- Computer Modern Serif-->'
        head += '<link rel="stylesheet" href="fonts/cmun-serif.css"></link>'
        head += '<link rel="stylesheet" href="index.css" type="text/css">\n'

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

        
        # Navbar
        body += '\n\n<!-- begin: navbar -->\n'
        body += '<nav class="navbar navbar-dark bg-primary mb-1">\n'
        body += '<div class="container-fluid">\n'
        body += '<a class="navbar-brand" href="main.html">Notas de Aula<br/><small>Política de Dados</small></a>\n'
        body += '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">\n'
        body += '<span class="navbar-toggler-icon"></span>\n'
        body += '</button>\n'
        body += '<div class="collapse navbar-collapse" id="navbarNav">\n'
        body += '<ul class="navbar-nav">\n'
        body += '<li class="nav-item"><a class="nav-link" href="index.html"><i class="fas fa-home"></i> Início</a></li>\n'
        body += '<li class="nav=item"><a class="nav-link" href="https://colab.research.google.com/github/phkonzen/notas/blob/master/notas.ipynb">Google Colab</a></li>\n'
        body += '<li class="nav-item dropdown">\n'
        body += '<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown">\n'
        body += 'Contato\n'
        body += '</a>\n'
        body += '<div class="dropdown-menu" aria-labelledby="navbarDropdown">\n'
        body += '<a class="dropdown-item" href="./contato.html"><i class="fas fa-envelope"></i> Mensagem</a>\n'
        body += '<a class="dropdown-item" href="https://www.instagram.com/notas.pedrok/"><i class="fab fa-instagram"></i> notas.pedrok</a>\n'
        body += '</div><!-- div class="dropdown-menu" aria-labelledby="navbarDropdown" -->\n'
        body += '</li> <!-- li class="nav-item dropdown" -->\n'
        body += '<li class="nav-item"><a class="nav-link" href="https://github.com/phkonzen/notas"><i class="fab fa-github" aria-hidden="true"></i> Repo</a></li>\n'
        body += '<li class="nav-item"><a class="nav-link active" href="./politica.html">Política de Dados</a></li>\n'
        body += '</ul>\n'
        body += '</div><!-- /.navbar-collapse -->\n'
        body += '</div><!-- /.container-fluid -->\n'
        body += '</nav>\n'
        body += '\n\n<!-- end: navbar -->\n\n\n'

        # redes sociais
        body += '<p class="text-left mb-0"><a href="./contato.html"><i class="fas fa-envelope"></i></a> | <a href="https://www.instagram.com/notas.pedrok/"><i class="fab fa-instagram"></i></a> | <a href="https://archive.org/details/notas-de-aula"><i class="fas fa-building-columns"></i></a> | <a href="https://www.youtube.com/channel/UCwutHKlKLgVj6IkFSUFBqoA"><i class="fab fa-youtube"></i></a> | <a href="https://github.com/phkonzen/notas"><i class="fab fa-github" aria-hidden="true"></i></a></p>\n\n\n'

        
        #miolo

        body += '<h3 class="mt-1">Política de uso de dados</h3>\n\n'

        body += '<p>Ao nagevar por este site, você concorda estar ciente da coleta de dados pela utilização de <i>cookies</i> e tecnologias semelhantes. O administrador deste <i>site</i> tem acesso apenas a dados anonimizados e agrupados, sendo estes utilizados para fins de melhorar a experiência de navegação dos usuários do <i>site</i>. Eventualmente, estes dados poderão ser utilizados na publicidade do <i>site</i>.</p>\n'

        body += '<h4 class="mt-1">Google Tag Manager</h4>\n\n'

        body += '<p>Este é um cookie usado para coletar dados referente aos acesso ao site para serem analisados pela ferramenta <a href="https://marketingplatform.google.com/about/analytics/?hl=en_US">Google Analytics</a>. Para mais informações, vise o site da ferramenta: <a href="https://marketingplatform.google.com/about/analytics">https://marketingplatform.google.com/about/analytics</a>.</p>'

        body += '<h4 class="mt-1">Formulário de contato</h4>\n\n'

        body += '<p>Ao utilizar o formulário de contato o usuário enviará os dados fornecidos para o e-mail do administrador deste <i>site</i>. O formulário utiliza a ferramenta <a href="https://formspree.io">Formspree</a>. Para mais informações, visite o <i>site</i>: <a href="https://formspree.io">https://formspree.io</a>.</p>'

        body += '<h4 class="mt-1">Contato</h4>\n\n'

        body += '<p>Para entrar em contato com o administrador deste <i>site</i>, use o <a href="contato.html">Formulário de contato</a> ou envie e-mail para phkonzen@gmail.com .</p>'

        # rodapé (id=rodape)
        f = open('rodape.html','r')
        body += f.read()
        f.close()

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
        f = open(self.odir + '/politica.html','w')
        f.write(self.page)
        f.close()
