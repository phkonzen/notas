#!/usr/bin/python3
'''
index.html

Autor: Pedro H A Konzen - 05/2018
Modificado: 03/2023
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
        head += '<title>Notas de Aula</title>\n'
        head += '<meta name="author" content="Pedro H A Konzen"/>\n'
        head += '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n'
        head += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">\n'
        head += '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>\n'
        head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>\n'
        

        # FontAwesome
        head += '<link href="./fontawesome/css/all.min.css" rel="stylesheet">'
        
        #google tracking
        f = open('gtag.js','r')
        head += f.read()
        f.close()
        
        head += '<!-- Computer Modern Serif-->'
        head += '<link rel="stylesheet" href="fonts/cmun-serif.css"></link>'
        head += '<link rel="stylesheet" href="index.css" type="text/css">\n'
        
        head += '</head>\n'

        #add at bottom
        self.page = self.page.replace('</html>',head)
        self.page += '</html>'

    def add_body(self):
        body = '<body>\n'
        
        body += '<div class="container-fluid mb-0">\n'
        body += '<div class="row">\n'
        body += '<div class="col-xl-1">\n'
        body += '</div>'
        body += '<div class="col-xl-10">\n\n'

        # colab alert (id=colabAlert)
        f = open('colab_alert.html','r')
        body += f.read()
        f.close()

        # general alert
        f = open('general_alert.html','r')
        body += f.read()
        f.close()
        
        # Navbar
        body += '\n\n<!-- begin: navbar -->\n'
        body += '<nav class="navbar navbar-dark bg-primary mb-1">\n'
        body += '<div class="container-fluid">\n'
        body += '<a class="navbar-brand" href="main.html">Notas de Aula<br/><small>Início</small></a>\n'
        body += '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">\n'
        body += '<span class="navbar-toggler-icon"></span>\n'
        body += '</button>\n'
        body += '<div class="collapse navbar-collapse" id="navbarNav">\n'
        body += '<ul class="navbar-nav">\n'
        body += '<li class="nav-item"><a class="nav-link active" href="index.html"><i class="fas fa-home"></i> Início</a></li>\n'
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
        body += '<li class="nav-item"><a class="nav-link" href="./politica.html">Política de dados</a></li>\n'
        body += '</ul>\n'
        body += '</div><!-- /.navbar-collapse -->\n'
        body += '</div><!-- /.container-fluid -->\n'
        body += '</nav>\n'
        body += '\n\n<!-- end: navbar -->\n\n\n'

        # redes sociais
        body += '<p class="text-left mb-0"><a href="./contato.html"><i class="fas fa-envelope"></i></a> | <a href="https://www.instagram.com/notas.pedrok/"><i class="fab fa-instagram"></i></a> | <a href="https://archive.org/details/notas-de-aula"><i class="fas fa-building-columns"></i></a> | <a href="https://www.youtube.com/channel/UCwutHKlKLgVj6IkFSUFBqoA"><i class="fab fa-youtube"></i></a> | <a href="https://github.com/phkonzen/notas"><i class="fab fa-github" aria-hidden="true"></i></a></p>\n\n\n'

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
        body += '<p class="mb-0" style="text-align: right; font-size: x-small;">Imagem: <a href="https://flic.kr/p/4krYcm">Eli Duke</a></p>\n'
        body += '</div> <!-- class="myjumbotron" -->\n'

        
        
        #miolo

        # Área de anúncios
        body += '<div id="demo" class="carousel slide" data-bs-ride="carousel" style="height: 3em;">'
        
        body += '<!-- The slideshow -->'
        body += '<div class="carousel-inner">\n'
        
        body += '<div class="carousel-item active">\n'
        body += '<div class="spinner-grow spinner-grow-sm text-warning mb-1" role="status"></div>\n'
        body += '<a href="https://wp.ufpel.edu.br/ermacrs23/">XI ERMAC-RS 2023 - Submissão de trabalhos: 01-31/março</a>\n'
        body += '</div>\n\n'

        body += '<div class="carousel-item">\n'
        body += '<div class="spinner-grow spinner-grow-sm text-primary mb-1" role="status"></div>\n'
        body += '<a href="https://www.ufrgs.br/ppgmap">PPGMAp - UFRGS: Mestrado e Doutorado</a>\n'
        body += '</div>\n\n'

        body += '<div class="carousel-item">\n'
        body += '<div class="spinner-grow spinner-grow-sm text-primary mb-1" role="status"></div>\n'
        body += '<a href="http://www.ufrgs.br/ime">IME - UFRGS: Instituto de Matemática e Estatística</a>\n'
        body += '</div>\n\n'
  
        body += '</div>\n'
        body += '</div>\n\n'

        body += '<h3 class="mt-1">Notas de Aula</h3>\n\n'
        body += '<hr>'

        body += '<div class="row row-col-auto">' #row-col-xxl-3 row-col-xl-3 row-col-lg-4 row-col-md-4 row-col-sm-6">\n'  d-flex justify-content-left
        # card: notas de aula de Cálculo I
        body += '<div class="col">'
        body += '<!-- card: notas de aula de Cálculo I -->\n'
        body += '<div class="card border-warning mb-3" style="width: 20rem;">\n'
        body += '<div class="card-header bg-warning">Notas de Aula <span class="badge bg-secondary">Python</span></div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Cálculo I</h5>\n'
        body += '<p class="card-text" style="color: gray">Cálculo diferencial e integral de funções de uma variável real</p>\n'
        body += '<a href="./CalculoI/main.html" class="btn btn-warning">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: notas de aula de EaD
        body += '<div class="col">'
        body += '<!-- card: notas de aula de EaD -->\n'
        body += '<div class="card border-primary mb-3" style="width: 20rem;">\n'
        body += '<div class="card-header bg-primary text-white">Notas de Aula <span class="badge bg-secondary">Python</span></div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Equações a Diferenças</h5>\n'
        body += '<p class="card-text" style="color: gray">Introdução a equações a diferenças</p>\n'
        body += '<a href="./EaD/main.html" class="btn btn-primary">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: notas de aula de EDO
        body += '<div class="col">'
        body += '<!-- card: notas de aula de EDO -->\n'
        body += '<div class="card border-primary mb-3" style="width: 20rem;">\n'
        body += '<div class="card-header bg-primary text-white">Notas de Aula <span class="badge bg-secondary">Python</span></div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Equações Diferencias Ordinárias</h5>\n'
        body += '<p class="card-text" style="color: gray">Introdução a equações diferenciais ordinárias</p>\n'
        body += '<a href="./EDO/main.html" class="btn btn-primary">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: Geometria analítica
        body += '<div class="col">'
        body += '<!-- card: Geometria analítica -->\n'
        body += '<div class="card border-primary mb-3" style="width: 20rem;">\n'
        body += '<div class="card-header bg-primary text-white">Notas de Aula</div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Geometria Analítica</h5>\n'
        body += '<p class="card-text" style="color: gray">Introdução à geometria analítica</p>\n'
        body += '<a href="./GeometriaAnalitica/main.html" class="btn btn-primary">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: notas de aula de Matemática numérica
        body += '<div class="col">'
        body += '<!-- card: notas de aula de Matemática numérica -->\n'
        body += '<div class="card border-primary mb-3" style="width: 20rem;">\n'
        body += '<div class="card-header bg-primary text-white">Notas de Aula <span class="badge bg-secondary">Octave</span></div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Matemática Numérica</h5>\n'
        body += '<p class="card-text" style="color: gray">Métodos e técnicas de cálculo numérico</p>\n'
        body += '<a href="./MatematicaNumerica/main.html" class="btn btn-primary">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: notas de aula de Matemática Numérica Avançada
        body += '<div class="col">'
        body += '<!-- card: notas de aula de Matemática numérica avançada -->\n'
        body += '<div class="card border-warning mb-3" style="width: 20rem;">\n'
        body += '<div class="card-header bg-warning text-dark">Notas de Aula <span class="badge bg-secondary">Python</span></div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Matemática Numérica Avançada</h5>\n'
        body += '<p class="card-text" style="color: gray">Tópicos de matemática numérica avançada</p>\n'
        body += '<a href="./MatematicaNumericaAvancada/main.html" class="btn btn-warning">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: notas de aula de Matemática Numérica Paralela
        body += '<div class="col">'
        body += '<!-- card: notas de aula de Matemática numérica paralela -->\n'
        body += '<div class="card border-primary mb-3" style="width: 20rem;">\n'
        body += '<div class="card-header bg-primary text-white">Notas de Aula <span class="badge bg-secondary">C/C++</span></div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Matemática Numérica Paralela</h5>\n'
        body += '<p class="card-text" style="color: gray">Introdução à computação paralela aplicada a métodos numéricos</p>\n'
        body += '<a href="./MatematicaNumericaParalela/main.html" class="btn btn-primary">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: Método de elementos finitos
        body += '<div class="col">'
        body += '<!-- card: Método de elementos finitos -->\n'
        body += '<div class="card border-primary mb-3" style="width: 20rem;">\n'
        body += '<div class="card-header bg-primary text-white">Notas de Aula <span class="badge bg-secondary">Python</span></div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Método de Elementos Finitos</h5>\n'
        body += '<p class="card-text" style="color: gray">Introdução ao método de elementos finitos</p>\n'
        body += '<a href="./MetodoElementosFinitos/main.html" class="btn btn-primary">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: Pré-Cálculo
        body += '<div class="col">'
        body += '<!-- card: Pré-Cálculo -->\n'
        body += '<div class="card border-warning mb-3" style="width: 20rem;">\n'
        body += '<div class="card-header bg-warning">Notas de Aula <span class="badge bg-secondary">Python</span></div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Pré-Cálculo</h5>\n'
        body += '<p class="card-text" style="color: gray">Matemática essencial para um curso de cálculo.</p>\n'
        body += '<a href="./PreCalculo/main.html" class="btn btn-warning">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: Vetores
        body += '<div class="col">'
        body += '<!-- card: Vetores -->\n'
        body += '<div class="card border-primary mb-3" style="width: 20rem;">\n'
        body += '<div class="card-header bg-primary text-white">Notas de Aula</div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Vetores</h5>\n'
        body += '<p class="card-text" style="color: gray">Vetores no espaço euclidiano tridimensional</p>\n'
        body += '<a href="./Vetores/main.html" class="btn btn-primary">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        body += '</div> <!-- div class=row-->\n\n'

        # Minicursos
        body += '<h3>Minicursos</h3>\n\n'
        body += '<hr>'
        
        body += '<div class="row row-col-auto">\n' #col-xxl-3 col-xl-3 col-lg-4 col-md-4 col-sm-6 d-flex justify-content-left

        # card: notas do Minicurso de Python para Matemática
        body += '<div class="col">'
        body += '<!-- card: notas do MiniPython -->\n'
        body += '<div class="card border-primary mb-3" style="width: 20rem;">\n'
        body += '<div class="card-header bg-primary text-white">Minicurso <span class="badge bg-secondary">Python</span></div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Python para Matemática</h5>\n'
        body += '<p class="card-text" style="color: gray">Introdução à Python para Matemática</p>\n'
        body += '<a href="./MiniPython/main.html" class="btn btn-primary">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: Mini Cálculo com Python
        body += '<div class="col">'
        body += '<!-- card: Mini Cálculo com python -->\n'
        body += '<div class="card border-primary mb-3" style="width: 20rem;">\n'
        body += '<div class="card-header bg-primary text-white">Minicurso <span class="badge bg-secondary">Python</span></div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title">Cálculo com Python</h5>\n'
        body += '<p class="card-text" style="color: gray">Introdução à Python na resolução de problemas de Cálculo I.</p>'
        body += '<ul>\n'
        body += '<li><a href="https://colab.research.google.com/github/phkonzen/notas/blob/master/docs/MiniCalcPy/1-funcoes.ipynb">Parte 1 - Funções de uma variável</a></li>\n'
        body += '<li><a href="https://colab.research.google.com/github/phkonzen/notas/blob/master/docs/MiniCalcPy/2-limites.ipynb">Parte 2 - Limites</a></li>\n'
        body += '<li><a href="https://colab.research.google.com/github/phkonzen/notas/blob/master/docs/MiniCalcPy/3-derivada.ipynb">Parte 3 - Derivadas</a></li>\n'
        body += '<li><a href="https://colab.research.google.com/github/phkonzen/notas/blob/master/docs/MiniCalcPy/4-integracao.ipynb">Parte 4 - Integrais</a></li>\n'
        body += '</ul>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'


        body += '</div> <!-- div class="row" -->\n'


        
        body += '<div class="row row-col-auto">\n'
        # body += '<div class="col-md-6">\n'

        body += '<h3>Vídeos & Áudios</h3>'
        body += '<hr>'

        # card: Internet Archive
        body += '<!-- card: Internet Archive -->\n'
        body += '<div class="col">'
        body += '<div class="card border-primary mb-3" style="width: 20rem;">\n'
        body += '<div class="card-header bg-primary text-white">Vídeos & Áudios</div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title"><i class="fas fa-building-columns"></i> Internet Archive</h5>\n'
        body += '<p class="card-text" style="color: gray">Coleção de vídeos e áudios das Notas de Aula no archive.org.</p>\n'
        body += '<a href="https://archive.org/details/notas-de-aula" class="btn btn-primary">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        # card: YouTube
        body += '<!-- card: YouTube -->\n'
        body += '<div class="col">'
        body += '<div class="card border-primary mb-3" style="width: 20rem;">\n'
        body += '<div class="card-header bg-primary text-white">Vídeos & Áudios <span class="badge bg-success">Novo</span></div>\n'
        body += '<div class="card-body">\n'
        body += '<h5 class="card-title"><i class="fab fa-youtube"></i> YouTube</h5>\n'
        body += '<p class="card-text" style="color: gray">Página das Notas de Aula no YouTube.</p>\n'
        body += '<a href="https://www.youtube.com/channel/UCwutHKlKLgVj6IkFSUFBqoA" class="btn btn-primary">\n'
        body += 'Abrir</a>\n'
        body += '</div>\n'
        body += '</div>\n'
        body += '</div>\n\n'

        
        #body += '</div><!-- div class="col-lg-3 ..." -->\n'
        
        body += '</div><!-- div class="row" -->\n'

        
        body += '<div class="row">\n' #row-col-md6

        body += '<div class="col-md-6">\n'

        body += '<h3>Sobre</h3>\n'
        body += '<hr>'
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
        body += '<hr>'
        body += '<ul>\n'
        body += '<li><a href="http://lattes.cnpq.br/2565213716047382">Currículo Lattes</a></li>\n'
        body += '<li><a href="http://professor.ufrgs.br/pedro/">Página de professor na UFRGS</a></li>\n'
        body += '</ul>\n'

        body += '<h3>Ligações Recomendadas</h3>\n'
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

        # body += '</div> <!-- div class="container-fluid" -->\n'

        body += '</div> <!-- div class=col-xl-10 -->\n'
        body += '<div class=col-xl-1>\n'
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
        #os.system('cp jumbotron.jpg '+self.odir+'/')
        #os.system('cp jumbotron2.jpg '+self.odir+'/')
        os.system('cp index.css '+self.odir+'/')
