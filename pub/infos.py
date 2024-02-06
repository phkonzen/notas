#!/usr/bin/python3
'''
infos.html

Autor: Pedro H A Konzen - 02/2024
'''

import os

class Infos:
    
    def __init__(self,odir):
        self.odir = odir
        self.page = ''
        
    def empty_page(self):
        self.page += '<!DOCTYPE html>'
        self.page += '<html lang="pt">'
        self.page += '</html>'

    def add_head(self):
        head = '<head>'
        
        head += '<meta charset="utf-8">'
        head += '<title>Notas de aula - Informações</title>'
        head += '<meta name="author" content="Pedro H A Konzen"/>'
        head += '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">'

        # bootstrap 5.3.0
        head += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">'
        head += '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>'
        
        # jquery 3.6.0
        head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>'
        
        # FontAwesome
        head += '<link href="./fontawesome/css/all.min.css" rel="stylesheet">'
        
        #google tracking
        f = open('gtag.js','r')
        head += f.read()
        f.close()

        head += '<!-- Computer Modern Serif-->'
        head += '<link rel="stylesheet" href="fonts/cmun-serif.css"></link>'
        head += '<link rel="stylesheet" href="index.css" type="text/css">'

        head += '</head>'

        #add at bottom
        self.page = self.page.replace('</html>',head)
        self.page += '</html>'

    def add_body(self):
        body = '<body>'
        
        body += '<div class=container-fluid>'
        body += '<div class=row>'
        body += '<div class=col-xxl-1>'
        body += '</div>'
        body += '<div class=col-xxl-10>'

        
        # Navbar
        body += '<!-- begin: navbar -->'
        body += '<nav class="navbar navbar-dark bg-primary mb-1">'
        body += '<div class="container-fluid">'
        body += '<a class="navbar-brand" href="infos.html">Notas de Aula<br/><small>Informações</small></a>'
        body += '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">'
        body += '<span class="navbar-toggler-icon"></span>'
        body += '</button>'
        body += '<div class="collapse navbar-collapse" id="navbarNav">'
        body += '<ul class="navbar-nav">'
        body += '<li class="nav-item"><a class="nav-link" href="index.html"><i class="fas fa-home"></i> Início</a></li>'
        body += '<li class="nav-item dropdown">'
        body += '<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown">'
        body += 'Contato'
        body += '</a>'
        body += '<div class="dropdown-menu" aria-labelledby="navbarDropdown">'
        body += '<a class="dropdown-item" href="./contato.html"><i class="fas fa-envelope"></i> Mensagem</a>'
        body += '<a class="dropdown-item" href="https://www.instagram.com/notas.pedrok/"><i class="fab fa-instagram"></i> notas.pedrok</a>'
        body += '</div><!-- div class="dropdown-menu" aria-labelledby="navbarDropdown" -->'
        body += '</li> <!-- li class="nav-item dropdown" -->'
        body += '<li class="nav-item"><a class="nav-link" href="https://github.com/phkonzen/notas"><i class="fab fa-github" aria-hidden="true"></i> Repo</a></li>'
        body += '<li class="nav-item"><a class="nav-link active" href="./infos.html#colabore"><i class="fa-solid fa-heart" style="color:red;"></i> Colabore</a></li>'
        body += '<li class="nav-item"><a class="nav-link" href="./infos.html#politica">Política de Dados</a></li>'
        body += '</ul>'
        body += '</div><!-- /.navbar-collapse -->'
        body += '</div><!-- /.container-fluid -->'
        body += '</nav>'
        body += '<!-- end: navbar -->'

        # redes sociais
        body += '<p class="text-left mb-0"><a href="./contato.html"><i class="fas fa-envelope"></i></a> | <a href="https://www.instagram.com/notas.pedrok/"><i class="fab fa-instagram"></i></a> | <a href="https://archive.org/details/notas-de-aula"><i class="fas fa-building-columns"></i></a> | <a href="https://www.youtube.com/channel/UCwutHKlKLgVj6IkFSUFBqoA"><i class="fab fa-youtube"></i></a> | <a href="https://github.com/phkonzen/notas"><i class="fab fa-github" aria-hidden="true"></i></a></p>'

        
        #miolo

        ## Como Colaborar
        body += '<h3 id="colabore" class="mt-3"><i class="fa-solid fa-heart" style="color:red;"></i> Colabore</h3>'
        body += '<p>Há várias <strong>formas de colaborar</strong> com as <a href="./main.html">Notas de Aula</a>!</p>'
        body += '<ul>'
        body += '<li>Envie <strong>avisos de erro</strong> ou <strong>sugestões</strong>...'
        body += '<ul>'
        body += '<li>usando o <a href="./contato.html"><i class="fas fa-envelope"></i> Formulário de Contato</a> do site.</li>'
        body += '<li>abrindo um novo <strong><i>Issue</i></strong> ou colaborando em um já aberto no <a href="https://github.com/phkonzen/notas"><i class="fab fa-github" aria-hidden="true"></i> GitHub Repo</a> do site.</li>'
        body += '</ul>'
        body += '<li><strong>Siga</strong> as Notas de Aula nas redes sociais <strong>e compartilhe</strong>!  <i class="far fa-smile-wink"></i>'
        body += '<ul>'
        body += '<li>Instagram: <a href="https://www.instagram.com/notas.pedrok/"><i class="fab fa-instagram"></i> notas.pedrok</a></li>'
        body += '<li>YouTube: <a href="https://www.youtube.com/channel/UCwutHKlKLgVj6IkFSUFBqoA"><i class="fab fa-youtube"></i> notas.pedrok</a></li>'
        body += '<li>GitHub: <a href="https://github.com/phkonzen/notas"><i class="fab fa-github" aria-hidden="true"></i> phkonzen/notas</a></li>'
        body += '</ul>'
        body += '</li>'
        body += '</ul>'

        ## Política de uso de dados
        body += '<hr>'
        body += '<h3 id="politica" class="mt-3">Política de Uso de Dados</h3>'

        body += '<p>Ao nagevar por este site, você concorda estar ciente da coleta de dados pela utilização de <i>cookies</i> e tecnologias semelhantes. O administrador deste <i>site</i> tem acesso apenas a dados anonimizados e agrupados, sendo estes utilizados para fins de melhorar a experiência de navegação dos usuários do <i>site</i>. Eventualmente, estes dados poderão ser utilizados na publicidade do <i>site</i>.</p>'

        body += '<h4 class="mt-1">Google Tag Manager</h4>'

        body += '<p>Este é um cookie usado para coletar dados referente aos acesso ao site para serem analisados pela ferramenta <a href="https://marketingplatform.google.com/about/analytics/?hl=en_US">Google Analytics</a>. Para mais informações, vise o site da ferramenta: <a href="https://marketingplatform.google.com/about/analytics">https://marketingplatform.google.com/about/analytics</a>.</p>'

        body += '<h4 class="mt-1">Formulário de Contato</h4>'

        body += '<p>Ao utilizar o formulário de contato o usuário enviará os dados fornecidos para o e-mail do administrador deste <i>site</i>. O formulário utiliza a ferramenta <a href="https://formspree.io">Formspree</a>. Para mais informações, visite o <i>site</i>: <a href="https://formspree.io">https://formspree.io</a>.</p>'

        body += '<h4 class="mt-1">Contato</h4>'

        body += '<p>Para entrar em contato com o administrador deste <i>site</i>, use o <a href="contato.html">Formulário de contato</a> ou envie e-mail para phkonzen@gmail.com .</p>'

        # rodapé (id=rodape)
        f = open('rodape.html','r')
        body += f.read()
        f.close()

        body += '</div> <!-- div class=col-lg-10 -->'
        body += '</div><!-- div row -->'
        body += '</div> <!-- div class=container-fluid -->'



        body += ''

        
        body += '</body>'

        #add at bottom
        self.page = self.page.replace('</html>',body)
        self.page += '</html>'

    def build(self):
        self.empty_page()
        self.add_head()
        self.add_body()
        f = open(self.odir + '/infos.html','w')
        f.write(self.page)
        f.close()
