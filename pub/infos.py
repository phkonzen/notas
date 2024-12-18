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
        head += '<title>NotasPedroK - Informações</title>'
        head += '<meta name="author" content="Pedro H A Konzen"/>'
        head += '<link rel="icon" type="image/x-icon" href="./pics/favicon.ico">'
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
        body += '<a class="navbar-brand" href="infos.html">NotasPedroK<br/><small>Informações</small></a>'
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
        body += '<p>'
        body += 'O site foi criado para o compartilhamento de minhas notas de aula com acesso livre e gratuito. Consulte as formas de colaboração e me ajude a manter o site livre, gratuito e sem propagandas.'
        body += '</p>'
        body += '<ul>'
        body += '<li><strong>Compre</strong> um dos livros das notas de aula!'
        body += '<ul>'
        body += '<li>Consulte os <a href="https://clubedeautores.com.br/livros/autores/pedro-henrique-de-almeida-konzen">livros impressos</a> disponíveis no <a href="https://clubedeautores.com.br/livros/autores/pedro-henrique-de-almeida-konzen">Clube de Autores</a></li>'
        body += '<li>Série de <a href="https://www.amazon.com.br/dp/B0CW18N6T5">e-books</a> das notas de aula na <a href="https://www.amazon.com.br/dp/B0CW18N6T5">Amazon.com.br</a>.</li>'
        body += '</ul>'
        body += '<li><strong>Envie um comentário</strong> avisando de erros, sugestões, críticas ...'
        body += '<ul>'
        body += '<li><a href="./contato.html"><i class="fas fa-envelope"></i> Formulário de Contato</a></li>'
        body += '<li><a href="https://github.com/phkonzen/notas"><i class="fab fa-github" aria-hidden="true"></i> GitHub Repo</a></li>'
        body += '</ul>'
        body += '<li><strong>Siga & compartilhe</strong> NotasPedroK nas redes sociais!</li>'
        body += '<ul>'
        body += '<li>Instagram: <a href="https://www.instagram.com/notas.pedrok/"><i class="fab fa-instagram"></i> notas.pedrok</a></li>'
        body += '<li>YouTube: <a href="https://www.youtube.com/channel/UCwutHKlKLgVj6IkFSUFBqoA"><i class="fab fa-youtube"></i> notas.pedrok</a></li>'
        body += '<li>GitHub: <a href="https://github.com/phkonzen/notas"><i class="fab fa-github" aria-hidden="true"></i> phkonzen/notas</a></li>'
        body += '</ul>'
        body += '</li>'
        body += '</ul>'

        ## Pq comprar?
        body += '<h3 class="mt-3"><i class="fa-solid fa-book-open"></i> Por que comprar um livro das notas de aula?</h3>'
        body += '<p> Além de colaborar com o site, os livros impressos oferecem uma experiência de leitura única, estão disponíveis em acabamento brochura com texto em colorido ou em preto e branco.</p>'
        body += '<h4>Qual título está disponível?</h4>'
        body += '<ul>'
        body += '<li><strong>Python para Matemática</strong>'
        body += '<p>Notas de aula de minicurso sobre a linguagem de programação Python. O livro traz uma introdução sobre os elementos da linguagem, da programação estruturada, da computação matricial e de gráficos. É pensada para estudantes de cursos de matemática e áreas afins.</p>'
        body += '</li>'
        body += '</ul>'


        body += '<h3 class="mt-3"><i class="fa-solid fa-tablet-screen-button"></i> Por que comprar um e-book das notas de aula?</h3>'
        body += '<ul>'
        body += '<li><strong>Seu e-book, sua escolha!</strong></li>'
        body += '<p>A qualquer momento, as notas de aula podem sofrer alterações de conteúdo (modificações, remoções, adições, correções, etc.). Mas, não se preocupe, seu e-book só é atualizado se e quado você quiser.</p>'
        body += '<li><strong>Conte com toda as vantagens de um e-book Kindle.</strong></li>'
        body += '<p>Os e-books das notas de aula estão disponíveis para o app Kindle, compatível com celulares e tablets (Android, IOS, entre outros), bem como disponível em computadores (Linux, Windows, entre outros). Assim você terá todos as vantagens de portabilidade, acessibilidade, sustentabilidade, economia e disponibilidade dos e-books Kindle.</p>'
        body += '<li><strong>Ajude a manter o site com acesso livre e sem propagandas.</strong></li>'
        body += '<p>Ao comprar um e-book das notas de aula, você ajuda a manter o site das notas de aula com acesso livre e sem propagandas.</p>'
        body += '</ul>'

        ## Política de uso de dados
        body += '<hr>'
        body += '<h3 id="politica" class="mt-3"><i class="fa-regular fa-file-lines"></i> Política de Uso de Dados</h3>'

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
