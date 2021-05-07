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
        head += '<title>Notas de aula</title>\n'
        head += '<meta name="author" content="Pedro H A Konzen"/>\n'
        head += '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n'

        # # BootstrapCDN v3.3
        # head += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n'
        # head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n'
        # head += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\n'

        #BootstrapCDN v.4.5
        # head += '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk"x crossorigin="anonymous">\n'

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
        body += '<nav class="navbar navbar-expand-md navbar-light bg-light mb-1">\n'
        body += '<a class="navbar-brand" href="main.html">Notas de Aula<br/><small>Início</small></a>\n'
        body += '<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">\n'
        body += '<span class="navbar-toggler-icon"></span>\n'
        body += '</button>\n'
        body += '<div class="collapse navbar-collapse" id="navbarNav">\n'
        body += '<ul class="navbar-nav">\n'
        body += '<li class="nav-item"><a class="nav-link" href="index.html"><i class="fas fa-home"></i> Início</a></li>\n'
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
        body += '<li class="nav-item active"><a class="nav-link" href="./politica.html">Política de dados</a></li>\n'
        body += '</ul>\n'
        body += '</div><!-- /.navbar-collapse -->\n'
        body += '</nav>\n'
        body += '\n\n<!-- end: navbar -->\n\n\n'
      
        
        #miolo

        body += '<h3 class="mt-1">Política de uso de dados</h3>\n\n'

        body += '<p>Ao nagevar por este site, você concorda estar ciente da coleta de dados pela utilização de <i>cookies</i> e tecnologias semelhantes. O administrador deste <i>site</i> tem acesso apenas a dados anonimizados e agrupados, sendo estes utilizados para fins de melhorar a experiência de navegação dos usuários do <i>site</i>. Eventualmente, estes dados poderão ser utilizados na publicidade do <i>site</i>.</p>\n'

        body += '<h4 class="mt-1">Google Tag Manager</h4>\n\n'

        body += '<p>Este é um cookie usado para coletar dados referente aos acesso ao site para serem analisados pela ferramenta <a href="https://marketingplatform.google.com/about/analytics/?hl=en_US">Google Analytics</a>. Para mais informações, vise o site da ferramenta: <a href="https://marketingplatform.google.com/about/analytics">https://marketingplatform.google.com/about/analytics</a>.</p>'

        body += '<h4 class="mt-1">Formulário de contato</h4>\n\n'

        body += '<p>Ao utilizar o formulário de contato o usuário enviará os dados fornecidos para o e-mail do administrador deste <i>site</i>. O formulário utiliza a ferramenta <a href="https://formspree.io">Formspree</a>. Para mais informações, visite o <i>site</i>: <a href="https://formspree.io">https://formspree.io</a>.</p>'

        body += '<h4 class="mt-1">Contato</h4>\n\n'

        body += '<p>Para entrar em contato com o administrador deste <i>site</i>, use o <a href="contato.html">Formulário de contato</a> ou envie e-mail para phkonzen@gmail.com .</p>'

        #rodapé
        body += '<div class="card">\n'
        body += '<div class="card-footer text-left">\n'
        body += '<i class="fa fa-github" aria-hidden="true"></i> GitHub Repo: '
        body += '<a href="https://github.com/phkonzen/notas" target="_blank">https://github.com/phkonzen/notas</a>. Contato '
        body += '<a href="contato.html" target="_blank"><i class="fas fa-envelope"></i></a>\n'
        body += '</div> <!-- div class="card" -->\n'
        body += '</div> <!-- div class="card-footer text-right" -->\n'


        body += '</div> <!-- div class=col-lg-10 -->\n'
        body += '<div class=col-lg-1>\n'
        body += '</div>\n'
        body += '</div><!-- div class=row -->\n'
        body += '</div> <!-- div class=container-fluid -->\n\n'


        body += '\n\n'
        # body += '<!-- JavaScript -->\n'
        # body += '<!-- jQuery first, then Popper.js, then Bootstrap JS -->\n'
        # body += '<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>\n'
        # body += '<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>\n'
        # body += '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>\n'

        
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
