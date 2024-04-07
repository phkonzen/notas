#!/usr/bin/python3

'''
Classe das notas de aula.

Autor: Pedro H A Konzen - 05/2018
Modificado: 02/2024
'''

import os

class Notas:

    def __init__(self):
        self.srcdir = ''
        self.odir = ''
        self.ebook = ''


    def goodies(self,htmldir,titulo_notas,srcref):

        # adiciona goodies.css
        f = open(htmldir+'/goodies.css','w')        
        text = 'body {'
        text += 'font-family: "Computer Modern Serif", serif;'
        text += '}'
        text += '@media (min-width: 576px) {'
        text += 'body {'
        text += 'font-size: larger;'
        text += '}'
        text += '}'

        text += '.ltx_title {'
        text += 'border-style: solid;'
        text += 'border-width: 0px 0px 1px 0px;'
        text += 'border-color: blueviolet;'
        text += '}'

        text += '.ltx_title_theorem {'
        text += 'border-style: dotted;'
        text += 'border-width: 0px 0px 2px 0px;'
        text += 'border-color: red;'
        text += '}'

        text += '.ltx_theorem {'
        text += 'border-style: dotted;'
        text += 'border-width: 0px 0px 2px 0px;'
        text += 'border-color: blue;'      
        text += '}'

        text += '.ltx_proof {'
        text += 'border-style: dotted;'
        text += 'border-width: 0px 0px 2px 0px;'
        text += 'border-color: blue;'      
        text += '}'

        text += '.ltx_title_proof {'
        text += 'border-style: dotted;'
        text += 'border-width: 0px 0px 2px 0px;'
        text += 'border-color: red;'      
        text += '}'

        text += '.ltx_verbatim {'
        text += 'font-size: 1em;'
        text += '}'

        text += '.ltx_listing {'
        text += 'overflow-x:none;'
        # text += 'border-style: dotted;'
        # text += 'border-width: 2px 0px;'
        # text += 'border-color: green;'
        text += 'display:block;'
        text += 'margin: 1ex 0em 1ex 0em;'
        text += 'text-align: left;'
        text += 'font-size: 1em;'
        text += '}'

        text += '.ltx_lstlisting {'
        text += 'margin: 1ex 0em 1ex 0em;'
        text += 'text-align: left;' 
        text += '}'

        text += '.ltx_float .ltx_listing {'
        text += 'margin: 0;' 
        text += '}'

        text += '.ltx_lstlisting {'
        text += 'white-space: normal;'
        text += 'word-break: break-all;'
        text += '}'

        text += '.ltx_listingline {'
        text += 'white-space: normal;'
        text += 'word-break: break-all;' 
        text += '}'
  
        text += '.ltx_lst_numbers_left .ltx_listingline .ltx_tag {'
        text += 'background-color:transparent;'
        text += 'margin-left: 0em;'
        text += 'width:2.5em;'
        text += 'margin-right:0.5em;'
        text += 'position: relative;'
        text += 'text-align:right;'
        text += '}'

        text += '.ltx_graphics {'
        text += 'max-width: 100%;'
        text += 'height: auto;'
        text += '}'

        # equations
        text += '.ltx_eqn_center_padleft {'
        # text += 'width: 0px;'
        text += 'min-width: 0px;'
        text += '}'

        # text += '.ltx_eqn_center_padleft {'
        # text += 'display: inherit;'
        # text += '}'

        # text += '.ltx_eqn_center_padright {'
        # text += 'width: 2em;'
        # text += '}'

        text += '.ltx_tabular {'
        text += 'max-width: 100%;'
        text += '}'

        text += '.ltx_ref {'
        text += 'margin: 0.25rem;'
        text += '}'

        f.write(text)
        f.close()
        
        #enxerta no __head__
        head = ''
        
        head += '<meta name="author" content="Pedro H A Konzen"/>'

        # bootstrap 5.3.0
        head += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">'
        head += '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>'

        # jquery 3.6.0
        head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>'
        
        # FontAwesome
        head += '<link href="../fontawesome/css/all.min.css" rel="stylesheet">'

        # Google icons
        # head += '<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">'
        head += '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200">'
        
        # Goodies CSS
        head += '<link rel="stylesheet" href="goodies.css" type="text/css">'


        # Google tracking
        f = open('gtag.js','r')
        head += f.read()
        f.close()

        head += '</head>'

        #enxerta no __body__ (top)
        body = '<body>'

        body += '<div class="container-fluid mb-0">'
        body += '<div class="row">'
        body += '<div class="col-xxl-1">'
        body += '</div>'
        body += '<div class="col-xxl-10">'

        # colab alert
        f = open('colab_alert.html','r')
        aux = f.read().replace('./infos.html','../infos.html')
        aux = aux.replace('<!-- subs:screen_rotation_icon -->',
                          '<span class="material-symbols-outlined m-0">screen_rotation</span>')
        body += aux
        f.close()

        # general alert
        f = open('general_alert.html','r')
        body += f.read().replace('./infos.html','../infos.html')
        f.close()

        
        # Navbar
        body += '<!-- begin: navbar -->'
        body += '<nav class="navbar navbar-dark bg-primary mb-1">'
        body += '<div class="container-fluid">'
        body += '<a class="navbar-brand" href="main.html">NotasPedroK<br/><small>'+titulo_notas+'</small></a>'
        body += '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">'
        body += '<span class="navbar-toggler-icon"></span>'
        body += '</button>'
        body += '<div class="collapse navbar-collapse" id="navbarNav">'
        body += '<ul class="navbar-nav">'
        body += '<li class="nav-item"><a class="nav-link" href="../index.html"><i class="fas fa-home"></i> Início</a></li>'
        body += '<li class="nav-item"><a class="nav-link active" href="main.html">Sumário</a></li>'
        body += '<li class="nav-item"><a class="nav-link" href="main.pdf"><i class="fas fa-download" aria-hidden="true"></i> PDF</a></li>'
        # body += '<li class="nav=item"><a class="nav-link" href="https://colab.research.google.com/github/phkonzen/notas/blob/master/notas.ipynb">Google Colab</a></li>'
        body += '<li class="nav-item dropdown">'
        body += '<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown">'
        body += 'Contato'
        body += '</a>'
        body += '<div class="dropdown-menu" aria-labelledby="navbarDropdown">'
        body += '<a class="dropdown-item" href="../contato.html"><i class="fas fa-envelope"></i> Mensagem</a>'
        body += '<a class="dropdown-item" href="https://www.instagram.com/notas.pedrok/"><i class="fab fa-instagram"></i> notas.pedrok</a>'
        body += '</div><!-- div class="dropdown-menu" aria-labelledby="navbarDropdown" -->'
        body += '</li> <!-- li class="nav-item dropdown" -->'
        body += '<li class="nav-item"><a class="nav-link" href="https://github.com/phkonzen/notas"><i class="fab fa-github" aria-hidden="true"></i> Repo</a></li>'
        body += '<li class="nav-item"><a class="nav-link" href="../infos.html#colabore"><i class="fa-solid fa-heart" style="color:red;"></i> Colabore</a></li>'
        body += '<li class="nav-item"><a class="nav-link" href="../infos.html#politica">Política de dados</a></li>'
        body += '</ul>'
        body += '</div><!-- /.navbar-collapse -->'
        body += '</div><!-- /.container-fluid -->'
        body += '</nav>'
        body += '<!-- end: navbar -->'

        # redes sociais
        body += '<p class="text-left mb-0"><a href="./contato.html"><i class="fas fa-envelope"></i></a> | <a href="https://www.instagram.com/notas.pedrok/"><i class="fab fa-instagram"></i></a> | <a href="https://archive.org/details/notas-de-aula"><i class="fas fa-building-columns"></i></a> | <a href="https://www.youtube.com/channel/UCwutHKlKLgVj6IkFSUFBqoA"><i class="fab fa-youtube"></i></a> | <a href="https://github.com/phkonzen/notas"><i class="fab fa-github" aria-hidden="true"></i></a> | <a href="https://www.amazon.com.br/dp/B0CW18N6T5"><i class="fab fa-amazon"></i></a></p>'
        
        #enxerta no __body__ (bottom)
        body_end = ''

        # rodapé (id=rodape)
        f = open('rodape.html','r')
        rp = f.read()
        f.close()
        body_end += rp.replace('./contato.html','../contato.html')
        
        body_end += '</div> <!-- div class=col-xxl-10 -->'
        body_end += '</div> <!-- div class=row -->'
        body_end += '</div> <!-- div class=container-fluid -->'

        body_end += '</body>'

        #enxerta no __footer

        # formulário de contato
        footer_top = ''
        footer_top = '<hr/>'
        footer_top += '<h3 class="mt-2"><i class="fa-solid fa-heart" style="color:red;"></i> Envie seu comentário</h3>'
        footer_top += '<p>As informações preenchidas são enviadas por e-mail para o desenvolvedor do site e tratadas de forma privada. Consulte a <a href="../infos.html#politica">Política de Use de Dados</a> para mais informações. Aproveito para agradecer a todas/os que de forma assídua ou esporádica contribuem enviando correções, sugestões e críticas! <i class="far fa-smile"></i></p>'
        f = open('formulario.html', 'r')
        footer_top += f.read()
        f.close()

        footer_bottom = ''
        footer_bottom += '<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Licença Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a><br />O texto acima está sob Licença <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/deed.pt_BR">Creative Commons Atribuição-CompartilhaIgual 4.0 Internacional</a>. '

        pages = []
        for (dirpath, dirnames, filenames) in os.walk(htmldir):
            pages.extend(filenames)
            break

        for p in pages:
            fn,ext = os.path.splitext(p)
            print('goodies em: %s', fn)
            if (ext == '.html'):
                print("goodies: affecting "+htmldir+"/"+p)
                #lê a página atual
                f = open(htmldir+"/"+p,'r')
                page = f.read()
                f.close()

                #modifica o __head__
                page = page.replace('</head>',head)

                #modifica o __body__ (top)
                page = page.replace('<body>',body)
                #modifica o __body__ (bottom)
                page = page.replace('</body>',body_end)

                merchant = '<p class="m-1" style="text-align: center">'
                merchant += '<i class="fa-solid fa-heart" style="color: red;"></i> '
                merchant += '<a href="'+self.ebook+'">Compre o livro deste material aqui!</a>'
                merchant += '</p>'

                if ((fn == 'main') and (self.ebook != '')):
                    page = page.replace('<div class="ltx_page_main">', f'{merchant}<div class="ltx_page_main">')

                if (fn != 'main'):
                    src_fname = fn
                    if (fn[0:4] == 'cap_'):
                        pos = fn.find('_sec')
                        if (pos != -1):
                            src_fname = fn[0:pos]

                        # book merchant
                        if (self.ebook != ''):
                            page = page.replace('</h1>',f'</h1>{merchant}')
    
                #     page = page.replace('</h1>',link_to_src+'</h1>')
                #     page = page.replace('</h2>',link_to_src+'</h2>')
                            
                

                    # tags

                    ## tag:remover (badge)
                    page = page.replace('[[tag:remover]]',
                                        '<span class="badge text-bg-danger">Em remoção</span>')
                    page = page.replace('[[badge:Em remoção]]',
                                        '<span class="badge text-bg-danger">Em remoção</span>')
                    
                    ## tag:revisar (badge)
                    page = page.replace('[[tag:revisar]]',
                                        '<span class="badge text-bg-warning">Em revisão</span>')
                    page = page.replace('[[badge:Em revisão]]',
                                        '<span class="badge text-bg-warning">Em revisão</span>')
                    
                    ## tag:contrucao (badge)
                    page = page.replace('[[tag:construcao]]',
                                        '<span class="badge text-bg-warning">Em construção</span>')
                    page = page.replace('[[badge:Em construção]]',
                                        '<span class="badge text-bg-warning">Em construção</span>')

                    # mídia com YouTube
                    i1 = page.find('[YouTube]')
                    while (i1 != -1):
                        yurl = '#'
                        vurl = '#'
                        aurl = '#'
                        
                        # YouTube URL
                        if (page[i1+9:i1+13] == '</a>'):
                            i2 = page.rindex('href="',0,i1)
                            f2 = page.index('"',i2+6,i1)
                            yurl = page[i2+6:f2]
                            print(yurl)

                            # raise ValeuError("Teste!")

                        # vídeo URL
                        i1 = page.index('[Vídeo]',i1)
                        if (page[i1+7:i1+11] == '</a>'):
                            i2 = page.rindex('href="',0,i1)
                            f2 = page.index('"',i2+6,i1)
                            vurl = page[i2+6:f2]
                            print(vurl)
                            
                        # áudio URL
                        i1 = page.index('[Áudio]',i1)
                        if (page[i1+7:i1+11] == '</a>'):
                            i2 = page.rindex('href="',0,i1)
                            f2 = page.index('"',i2+6,i1)
                            aurl = page[i2+6:f2]
                            print(aurl)
                            
                        # remove
                        i2 = page.rindex('<div ',0,i1)
                        f2 = page.index('</div>',i1)
                        print('rv: ', page[i2:f2+6])
                        page = page[0:i2] + \
                            '<!-- inc mídia -->' + \
                            page[f2+6:len(page)]

                        inc = ''
                        if ((yurl != '#') or (vurl != '#') or (aurl != '#')):
                            inc += '<div class="container d-flex justify-content-center mb-2">'
                            inc += '<div class="row">'
                            inc += '<div class="col-md-6">'
                            inc += '<a href="' + yurl + '" target="_blank"><img src="../pics/play_video.jpeg" class="card-img-top" alt="Assistir vídeo!" style="max-width: 20rem"></a>'
                            inc += '</div>'
                            inc += '<div class="col-md-6">'
                            inc += '<ul class="list-group list-group-flush  d-inline-flex">'
                            if (yurl != "#"):
                                inc += '<a href="' + yurl + '" target=_blank' + \
                                    ' class="list-group-item list-group-item-action text-primary"><i class="fab fa-youtube fa-xl"></i> Assista no YouTube!</a>'
                            else:
                                inc += '<a href="#" class="list-group-item list-group-item-action list-group-item-light"><i class="fab fa-youtube fa-xl"></i> Assista no YouTube</a>'
                            

                            if (vurl != "#"):
                                inc += '<a href="' + vurl +  '" target=_blank' + \
                                    ' class="list-group-item list-group-item-action text-primary"><i class="fas fa-building-columns fa-xl"></i> Assista no archive.org!</a>'
                            else:
                                inc += '<a href="#" class="list-group-item list-group-item-action list-group-item-light"><i class="fas fa-building-columns fa-xl"></i> Assista no archive.org!</a>'
                                
                            if (aurl != "#"):
                                inc += '<a href="' + aurl +  '" target=_blank' + \
                                    ' class="list-group-item list-group-item-action text-primary"><i class="fas fa-file-audio fa-xl"></i> Escute a audioleitura!</a></a>'
                            else:
                                inc += '<a href="#" class="list-group-item list-group-item-action list-group-item-light"><i class="fas fa-file-audio fa-xl"></i> Escute a audioleitura!</a></a>'
                            
                            inc += '</ul>'
                            inc += '</div>'
                            inc += '</div>'
                            inc += '</div>'


                        page = page.replace('<!-- inc mídia -->', inc);

                        i1 = page.find('[YouTube]')

                    # mídia sem Youtube
                    i1 = page.find('[Vídeo]')
                    while (i1 != -1):
                        yurl = '#'
                        vurl = '#'
                        aurl = '#'

                        # vídeo URL
                        i1 = page.index('[Vídeo]',i1)
                        if (page[i1+7:i1+11] == '</a>'):
                            i2 = page.rindex('href="',0,i1)
                            f2 = page.index('"',i2+6,i1)
                            vurl = page[i2+6:f2]
                            print(vurl)
                            
                        # áudio URL
                        i1 = page.index('[Áudio]',i1)
                        if (page[i1+7:i1+11] == '</a>'):
                            i2 = page.rindex('href="',0,i1)
                            f2 = page.index('"',i2+6,i1)
                            aurl = page[i2+6:f2]
                            print(aurl)
                            
                        # remove
                        i2 = page.rindex('<div ',0,i1)
                        f2 = page.index('</div>',i1)
                        print('rv: ', page[i2:f2+6])
                        page = page[0:i2] + \
                            '<!-- inc mídia -->' + \
                            page[f2+6:len(page)]

                        inc = ''
                        if ((yurl != '#') or (vurl != '#') or (aurl != '#')):
                            inc += '<div class="container d-flex justify-content-center mb-2">'
                            inc += '<div class="row">'
                            inc += '<div class="col-md-6">'
                            inc += '<a href="' + vurl + '" target="_blank"><img src="../pics/play_video.jpeg" class="card-img-top" alt="Assistir vídeo!" style="max-width: 20rem"></a>'
                            inc += '</div>'
                            inc += '<div class="col-md-6">'
                            inc += '<ul class="list-group list-group-flush  d-inline-flex">'
                            if (yurl != "#"):
                                inc += '<a href="' + yurl +  '" target=_blank' + \
                                    ' class="list-group-item list-group-item-action text-primary"><i class="fab fa-youtube fa-xl"></i> Assista no YouTube!</a>'
                            else:
                                inc += '<a href="#" class="list-group-item list-group-item-action list-group-item-light"><i class="fab fa-youtube fa-xl"></i> Assista no YouTube</a>'
                            

                            if (vurl != "#"):
                                inc += '<a href="' + vurl +  '" target=_blank' + \
                                    ' class="list-group-item list-group-item-action text-primary"><i class="fas fa-building-columns fa-xl"></i> Assista no archive.org!</a>'
                            else:
                                inc += '<a href="#" class="list-group-item list-group-item-action list-group-item-light"><i class="fas fa-building-columns fa-xl"></i> Assista no archive.org!</a>'
                            
                            if (aurl != "#"):
                                inc += '<a href="' + aurl +  '" target=_blank' + \
                                    ' class="list-group-item list-group-item-action text-primary"><i class="fas fa-file-audio fa-xl"></i> Escute a audioleitura!</a></a>'
                            else:
                                inc += '<a href="#" class="list-group-item list-group-item-action list-group-item-light"><i class="fas fa-file-audio fa-xl"></i> Escute a audioleitura!</a></a>'
                            
                            inc += '</ul>'
                            inc += '</div>'
                            inc += '</div>'
                            inc += '</div>'

                        page = page.replace('<!-- inc mídia -->', inc);

                        i1 = page.find('[Vídeo]')

                    
                #colapsa as respostas dos exercícios
                paux = page.find('ltx_theorem_resp')
                while (paux != -1):
                    pini = page[paux:0:-1].find('<')
                    pini = paux - pini
                    pter = paux+len('ltx_theorem_resp')+2
                    taux = page[pini:pter]
                    paux = taux.index('id="')+4
                    respid = taux[paux:]
                    paux = respid.index('"')
                    respid = respid[0:paux]
                    page = page.replace(taux, \
                                        '<div class="d-grid gap-2 d-md-flex justify-content-md-end">' + \
                                        '<button class="btn btn-warning" type="button" ' + \
                                        'data-bs-toggle="collapse" data-bs-target="#' + \
                                        respid + '">Resposta</button></div>' + \
                                        '<div class="collapse" id="'+respid+'">')
                    paux = page.find('ltx_theorem_resp')
                    
                #modifica o __footer__
                page = page.replace('<footer class="ltx_page_footer">',
                                    footer_top + '<footer class="ltx_page_footer">')
                page = page.replace('<div class="ltx_page_logo">',
                                    footer_bottom + '<div class="ltx_page_logo">')

                               
                #sobrescreve a página com as alterações
                f = open(htmldir+"/"+p,'w')
                f.write(page)
                f.close()

        # make index.html
        os.system('cp ' + htmldir+'/main.html ' + htmldir+'/index.html')

        
