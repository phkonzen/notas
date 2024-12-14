#!/usr/bin/python3
'''
index.html

Autor: Pedro H A Konzen - 05/2018
Modificado: 03/2024
'''

import os

class Index:
    
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
        head += '<title>NotasPedroK</title>'
        head += '<meta name="author" content="Pedro H A Konzen">'
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
        head += '<link rel="stylesheet" href="fonts/cmun-serif.css">'
        head += '<link rel="stylesheet" href="index.css" type="text/css">'
        
        head += '</head>'

        #add at bottom
        self.page = self.page.replace('</html>',head)
        self.page += '</html>'

    def new_card(self, header, title, 
                 text, badges, link, color, 
                 status="", ebook="", livro=""):
        card = ""
        card += f'<div class="card border-{color} mb-3" style="width: 21rem;">'
        card += f'<div class="card-header text-bg-{color} d-flex justify-content-between">{header} '
        if (status == "Atualizando"):
            card += f'<div class="spinner-border text-light" role="status"><span class="sr-only">Em atualização ...</span></div>'
        elif (status == "Novo"):
            card += f'<span class="align-middle"><span class="badge rounded-pill text-bg-light">{status}</span></span><div class="spinner-border text-light" role="status"><span class="sr-only">Loading...</span></div>'
        elif (status != ""):
            card += f'<span class="align-middle"><span class="badge rounded-pill text-bg-light">{status}</span></span>'
            
        card += '</div>'
        card += '<div class="card-body">'
        card += f'<h4 class="card-title">{title}</h4>'
        card += f'<p class="card-text" style="color: gray">{text}'
        for i,b in enumerate(badges):
            card += f'<span class="badge bg-secondary m-1">{b}</span>'
        card += '</p>'
        # buttons

        if (ebook != "") or (livro != ""):
            card += '<div class="d-flex justify-content-between">'

            if (ebook != ""):
                card += f'<a href="{ebook}" class="btn btn-outline-primary d-flex justify-content-between align-items-center">'
                card += '<span class="m-1"><p class="mb-0" style="font-size: 75%;"><i class="fa-solid fa-heart" style="color: red;"></i> Comprar</p><p class="mt-0 mb-0"><i class="fa-solid fa-tablet-screen-button"></i> E-book</p></span>'
            
            if (livro != ""):
                card += f'<a href="{livro}" class="btn btn-outline-primary d-flex justify-content-between align-items-center">'
                card += '<span class="m-1"><p class="mb-0" style="font-size: 75%;"><i class="fa-solid fa-heart" style="color: red;"></i> Comprar</p><p class="mt-0 mb-0"><i class="fa-solid fa-book-open"></i> Livro</p></span>'
        else:
            card += '<div class="d-flex justify-content-end">'

        card += f'<a href="{link}" class="btn btn-outline-success  d-flex align-self-end justify-content-between align-items-center">'
        card += '<i class="fa-solid fa-book-open-reader" style="color: green;"></i>'
        card += '<span class="m-1"><p class="mb-0" style="font-size: 75%;">Acesso</p><p class="mt-0 mb-0">Livre</p></span>'
        card += '</a>'
        card += '</div>'
        card += '</div>'
        card += '</div>'
        return card

    def add_anuncio(self, text, link, status):
        obj = ""
        # obj += f'<div class="card border-{status} d-flex justify-content-center" role="alert" style="height: 4em">'
        obj += f'<div class="card bg-light border-{status} d-flex justify-content-center" role="alert" style="height: 4em">'
        # obj += f'<div class="card-text text-{status} d-flex align-self-center">'
        obj += f'<div class="card-text text-{status} d-flex align-self-center">'
        obj += f'<a href={link} class="stretched-link"></a>'
        obj += f'<div class="spinner-grow spinner-grow-sm m-1" role="status"></div>'
        obj += f'<span class="text-primary">{text}</span>'
        obj += '</div>'
        obj += '</div>'
        return obj


    def add_body(self):
        body = '<body>'
        
        body += '<div class="container-fluid mb-0">'
        body += '<div class="row">'
        body += '<div class="col-xxl-1">'
        body += '</div>'
        body += '<div class="col-xxl-10">'

        # colab alert (id=colabAlert)
        f = open('colab_alert.html','r')
        body += f.read()
        f.close()

        # general alert
        f = open('general_alert.html','r')
        body += f.read()
        f.close()
        
        # Navbar
        body += '<!-- begin: navbar -->'
        body += '<nav class="navbar navbar-dark bg-primary mb-1">'
        body += '<div class="container-fluid">'
        body += '<a class="navbar-brand" href="index.html">NotasPedroK<br/><small>Início</small></a>'
        body += '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">'
        body += '<span class="navbar-toggler-icon"></span>'
        body += '</button>'
        body += '<div class="collapse navbar-collapse" id="navbarNav">'
        body += '<ul class="navbar-nav">'
        body += '<li class="nav-item"><a class="nav-link active" href="index.html"><i class="fas fa-home"></i> Início</a></li>'
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
        body += '<li class="nav-item"><a class="nav-link" href="./infos.html#colabore"><i class="fa-solid fa-heart" style="color:red;"></i> Colabore</a></li>'
        body += '<li class="nav-item"><a class="nav-link" href="./infos.html#politica">Política de dados</a></li>'
        body += '</ul>'
        body += '</div><!-- /.navbar-collapse -->'
        body += '</div><!-- /.container-fluid -->'
        body += '</nav>'
        body += '<!-- end: navbar -->'

        # redes sociais
        body += '<p class="text-left mb-0"><a href="./contato.html"><i class="fas fa-envelope"></i></a> | <a href="https://www.instagram.com/notas.pedrok/"><i class="fab fa-instagram"></i></a> | <a href="https://archive.org/details/notas-de-aula"><i class="fas fa-building-columns"></i></a> | <a href="https://www.youtube.com/channel/UCwutHKlKLgVj6IkFSUFBqoA"><i class="fab fa-youtube"></i></a> | <a href="https://github.com/phkonzen/notas"><i class="fab fa-github" aria-hidden="true"></i></a></p>'

        # # jumbotron
        # body += '<div class="myjumbotron">'
        # body += '<div class="jumbotron text-center">'
        # body += '<div class="row">'
        # body += '<div class="col-lg-3 col-md-2">'
        # body += '</div>'
        # body += '<div class="col-lg-6 col-md-8 ">'
        # body += '<h1 class="display-4 bg-white text-dark mb-0" style="opacity:75%;">Notas de Aula</h1>'
        # body += '<p class="lead bg-white text-dark mt-0" style="opacity:75%;">Pedro H A Konzen</p>'
        # body += '</div>'
        # body += '</div>'
        # body += '</div> <!-- div class="jumbotron text-center" -->'
        # body += '<p class="mb-0" style="text-align: right; font-size: x-small;">Imagem: <a href="https://flic.kr/p/4krYcm">Eli Duke</a></p>'
        # body += '</div> <!-- class="myjumbotron" -->'

        
        
        #miolo

        # Área de anúncios
        body += '<div id="demo" class="carousel slide mt-2 mb-2" data-bs-ride="carousel" style="height: 4em;">'

        body += '<!-- The slideshow -->'
        body += '<div class="carousel-inner">'

        # anúncio
        body += '<div class="carousel-item">'
        body += self.add_anuncio(text = 'XXVI Escola de Verão PPGMPA/UFSC: Inscrições até 13/Dez',
                                 link = 'https://sites.google.com/view/escoladevero/',
                                 status = 'danger')
        body += '</div>'

        # anúncio
        body += '<div class="carousel-item">'
        body += self.add_anuncio(text = 'XII ERMAC-RS 2025: Submissões até 15/Fev',
                                 link = 'https://sites.google.com/view/ermacrs',
                                 status = 'primary')
        body += '</div>'


        # anúncio
        body += '<div class="carousel-item active">'
        body += self.add_anuncio(text = 'PPG Matemática Aplicada: Seleção de Mestrado 25/1 até 17/Jan',
                                 link = 'https://www.ufrgs.br/ppgmap',
                                 status = 'warning')
        body += '</div>'


        # anúncio
        body += '<div class="carousel-item">'
        body += self.add_anuncio(text = 'Instituto de Matemática e Estatística - UFRGS',
                                 link = 'http://www.ufrgs.br/ime',
                                 status = 'primary')
        body += '</div>'

        body += '</div>'
        body += '</div>'


        # *** NOTAS DE AULA ***

        body += '<h3 class="">Notas de Aula</h3>'
        body += '<hr>'

        body += '<div class="row row-cols-auto justify-content-around">'

        # card: notas de aula de Algoritmos e Programação I
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Algoritmos e Programação I",
                              text = "Introdução aos algoritmos de programação de computadores",
                              badges = ["Python", "NumPy", "Matplotlib"],
                              link = "AlgoritmosProgramacaoI/main.html",
                              color = "primary", status = "",
                              ebook="https://a.co/d/eRjID1A")
        body += '</div>'

        # card: notas de aula de Cálculo I
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Cálculo I",
                              text = "Cálculo diferencial e integral de funções de uma variável real",
                              badges = ["Python", "Sympy"],
                              link = "CalculoI/main.html",
                              color = "primary", status = "")
        body += '</div>'

        # card: notas de aula de EaD
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Equações a Diferenças",
                              text = "Introdução a equações a diferenças",
                              badges = ["Python", "Sympy"],
                              link = "EaD/main.html",
                              color = "primary", status = "")
        body += '</div> '

        # card: notas de aula de EDO
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Equações Diferenciais Ordinárias",
                              text = "Introdução a equações diferenciais ordinárias",
                              badges = ["Python", "Sympy"],
                              link = "EDO/main.html",
                              color = "primary", status = "")
        body += '</div>'


        # card: Geometria analítica
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Geometria Analítica",
                              text = "Introdução à geometria analítica",
                              badges = [],
                              link = "GeometriaAnalitica/main.html",
                              color = "primary", status = "")
        body += '</div>'

        # card: notas de aula de Matemática Numérica Avançada
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Matemática Numérica Avançada",
                              text = "Tópicos de métodos numéricos avançados",
                              badges = ["Python", "NumPy", "SciPy", "Matplotlib"],
                              link = "MatematicaNumericaAvancada/main.html",
                              color = "secondary", status = "Antigo")
        body += '</div>'

        # card: notas de aula de Matemática Numérica I
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Matemática Numérica I",
                              text = "Introdução a métodos numéricos para resolução de equações e para aproximação de funções",
                              badges = ["Python", "NumPy"],
                              link = "MatematicaNumericaI/main.html",
                              color = "warning", status = "Atualizando")
        body += '</div>'

        # card: notas de aula de Matemática Numérica II
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Matemática Numérica II",
                              text = "Introdução a métodos numéricos para o cálculo de funções e resolução de equações diferenciais",
                              badges = ["Python", "NumPy"],
                              link = "MatematicaNumericaII/main.html",
                              color = "warning", status = "Atualizando")
        body += '</div>'

        # card: notas de aula de Matemática Numérica III
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Matemática Numérica III",
                              text = "Introdução a métodos numéricos para o cálculo de funções e resolução de equações diferenciais",
                              badges = ["Python", "NumPy"],
                              link = "MatematicaNumericaIII/main.html",
                              color = "warning", status = "Atualizando")
        body += '</div>'

        # card: notas de aula de Matemática Numérica Paralela
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Matemática Numérica Paralela",
                              text = "Introdução à computação paralela a métodos numéricos",
                              badges = ["C/C++", "OpenMP", "OpenMPI"],
                              link = "MatematicaNumericaParalela/main.html",
                              color = "primary", status = "")
        body += '</div>'

        # card: Método de Elementos Finitos
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Método dos Elementos Finitos",
                              text = "Introdução ao método dos elementos finitos",
                              badges = ["Python", "FEniCSx"],
                              link = "MetodoElementosFinitos/main.html",
                              color = "primary", status = "")
        body += '</div>'

        # card: Pré-Cálculo
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Pré-Cálculo",
                              text = "Matemáticas essencial para um curso de cálculo",
                              badges = ["Python", "SymPy"],
                              link = "PreCalculo/main.html",
                              color = "primary", status = "")
        body += '</div>'

        # card: Redes Neurais Artificiais
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Redes Neurais Artificiais",
                              text = "Introdução às Redes Neurais Artificiais",
                              badges = ["Python", "PyTorch"],
                              link = "RedesNeuraisArtificiais/main.html",
                              color = "warning", status = "Novo")
        body += '</div>'

        # card: Vetores
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Vetores",
                              text = "Vetores no espaço euclidiano tridimensional",
                              badges = [],
                              link = "Vetores/main.html",
                              color = "primary", status = "")
        body += '</div>'


        body += '</div> <!-- div class=row-->'

        # Minicursos
        body += '<h3>Minicursos</h3>'
        body += '<hr>'
        
        body += '<div class="row row-cols-auto justify-content-around">'

        # card: notas do Minicurso de Python para Matemática
        body += '<div class="col">'
        body += self.new_card(header = "Minicursos",
                              title = "Python para Matemática",
                              text = "Introdução à Python para matemática",
                              badges = ["Python", "NumPy", "Matplotlib"],
                              link = "MiniPython/main.html",
                              color = "primary", status = "",
                              ebook="https://www.amazon.com.br/dp/B0DMPQ24VY",
                              livro="https://clubedeautores.com.br/book/738083--Python_para_matematica")
        body += '</div>'

        # card: notas do Minicurso de C/C++ para Matemática
        body += '<div class="col">'
        body += self.new_card(header = "Minicursos",
                              title = "C/C++ para Matemática",
                              text = "Introdução às linguagens C/C++ para matemática",
                              badges = ["C/C++", "GSL"],
                              link = "MiniCpp/main.html",
                              color = "primary", status = "")
        body += '</div>'

        # card: Mini Cálculo com Python
        body += '<div class="col">'

        body += '<!-- card: Mini Cálculo com Python -->'
        body += '<div class="card border-primary mb-3" style="width: 21rem;">'

        body += '<div class="card-header bg-primary text-white">Minicurso <span class="badge bg-secondary">Python</span></div>'

        body += '<div class="card-body">'
        body += '<h4 class="card-title">Cálculo com Python</h4>'
        body += '<p class="card-text" style="color: gray">Introdução à Python na resolução de problemas de Cálculo I.</p>'
        body += '<ul>'
        body += '<li><a href="https://colab.research.google.com/github/phkonzen/notas/blob/master/docs/MiniCalcPy/1-funcoes.ipynb">Parte 1 - Funções de uma variável</a></li>'
        body += '<li><a href="https://colab.research.google.com/github/phkonzen/notas/blob/master/docs/MiniCalcPy/2-limites.ipynb">Parte 2 - Limites</a></li>'
        body += '<li><a href="https://colab.research.google.com/github/phkonzen/notas/blob/master/docs/MiniCalcPy/3-derivada.ipynb">Parte 3 - Derivadas</a></li>'
        body += '<li><a href="https://colab.research.google.com/github/phkonzen/notas/blob/master/docs/MiniCalcPy/4-integracao.ipynb">Parte 4 - Integrais</a></li>'
        body += '</ul>'
        body += '</div>'

        body += '</div>'
        body += '</div>'

        body += '</div> <!-- div class="row" -->'

        
        body += '<h3>Vídeos & Áudios</h3>'
        body += '<hr>'

        body += '<div class="row row-cols-auto justify-content-around">'

        # card: Internet Archive
        body += '<!-- card: Internet Archive -->'
        body += '<div class="col">'
        body += self.new_card(header = "Vídeos & Áudios",
                              title = '<i class="fas fa-building-columns"></i> Internet Archive',
                              text = "Coleção de vídeos e áudios das Notas de Aula no archive.org",
                              badges = [],
                              link = "https://archive.org/details/notas-de-aula",
                              color = "primary")
        body += '</div>'

        # card: YouTube
        body += '<!-- card: YouTube -->'
        body += '<div class="col">'
        body += self.new_card(header = "Vídeos & Áudios",
                              title = '<i class="fab fa-youtube"></i> YouTube',
                              text = "Coleção de vídeos das Notas de Aula no YouTube",
                              badges = [],
                              link = "https://www.youtube.com/channel/UCwutHKlKLgVj6IkFSUFBqoA",
                              color = "primary")
        body += '</div>'

        
        body += '</div><!-- div class="row" -->'

        
        body += '<div class="row">'

        body += '<div class="col-md-6">'

        body += '<h3>Sobre</h3>'
        body += '<hr>'
        body += '<p>NotasPedroK é o site de minhas notas de aula. '
        body += 'Escritos predominante em linguagem de marcação '
        body += '<a href="https://www.latex-project.org/">LaTeX</a>, '
        body += 'os textos são disponibilizados sob licença '
        body += '<a href="http://creativecommons.org/licenses/by-sa/4.0/deed.pt_BR">CC-BY-SA 4.0</a>. '
        body += 'Os códigos-fonte podem ser obtidos no '
        body += 'repositório GitHub '
        body += '<a href="https://github.com/phkonzen/notas">https://github.com/phkonzen/notas</a>.</p>'
        body += '<p>Aproveito para agradecer a todas/os que de forma assídua ou esporádica '
        body += 'contribuem com o material do site. Consulte as <a href="infos.html">formas de colaboração</a> e me ajude a manter o site livre, gratuito e sem propagandas! '
        body += '<i class="far fa-smile"></i>'
        body += '</p>'

        body += '</div><!-- div class="col-md-6" -->'

        body += '<div class="col-md-6">'

        body += '<h3>Sobre mim?</h3>'
        body += '<hr>'
        body += '<ul>'
        body += '<li><a href="http://lattes.cnpq.br/2565213716047382">Currículo Lattes</a></li>'
        body += '<li><a href="http://professor.ufrgs.br/pedro/">Página de professor na UFRGS</a></li>'
        body += '</ul>'

        # body += '<h3>Ligações Recomendadas</h3>'
        # body += '<ul>'
        # body += '<li><a href="https://archive.org/">Internet Archive</a>: biblioteca de milhões de livros, filmes, <i>softwares</i>, música, <i>websites</i> e mais</li>'
        # body += '<li><a href="https://www.geogebra.org/">Geogebra</a>: aplicativos abertos de matemática</li>'
        # body += '<li><a href="https://www.ufrgs.br/reamat">REAMAT</a>: projeto de recursos educacionais abertos de matemática</li>'
        # body += '</ul>'

        body += '</div><!-- div class="col-md-6" -->'

        body += '</div><!-- div class="row" -->'

        # rodapé (id=rodape)
        f = open('rodape.html','r')
        body += f.read()
        f.close()

        body += '</div> <!-- div class=col-xxl-10 -->'
        # body += '<div class=col-xl-1>'
        # body += '</div>'
        body += '</div><!-- div row -->'
        body += '</div> <!-- div class=container-fluid -->'

        body += '</body>'


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

        os.system('cp index.css '+self.odir+'/')
