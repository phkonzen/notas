#!/usr/bin/python3

'''
Classe das notas de aula.

Autor: Pedro H A Konzen - 05/2018
Modificado: 05/2021
'''

import os

class Notas:

    def __init__(self):
        raise ValueError("Você não devia estar aqui!!!")

    def goodies(self,htmldir,titulo_notas,srcref):

        # adiciona goodies.css
        f = open(htmldir+'/goodies.css','w')
        text = '* {\n'
        text += 'font-family: "Computer Modern Serif", serif;\n'
        text += '}\n\n'

        text += '.ltx_lst_numbers_left .ltx_listingline .ltx_tag {\n'
        text += 'margin-left: 0em;\n'
        text += 'text-align: right;\n'
        text += 'position: relative;\n'
        text += '}\n\n'
        
        text += '.navbar {\n'
        text += 'height: auto;\n'
        text += 'padding: 5px;\n'
        text += '}\n\n'

        # if (srcref != 'MatematicaNumericaParalela'):
        #     text += '.ltx_lst_numbers_left .ltx_listingline .ltx_tag {\n'
        #     text += 'margin-left:-1em; width:2.5em;\n'
        #     text += 'text-align:right; }\n'
        
        f.write(text)
        f.close()
        
        #enxerta no __head__
        head = ''
        
        head += '<meta name="author" content="Pedro H A Konzen"/>\n'
        head += '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n'

        #BootstrapCDN v.4.5
        #head += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">\n'
        #head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>\n'
        #head += '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>\n'
        #head += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>\n'

        #BootstrapCDN v.5.1
        head += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">\n'
        head += '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>\n'
        head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>\n'

        
        # FontAwesome
        # head += '<script src="https://kit.fontawesome.com/dfbff2c7ed.js" crossorigin="anonymous"></script>'
        head += '<link href="../fontawesome/css/all.css" rel="stylesheet">'
        head += '<link href="../fontawesome/css/brands.css" rel="stylesheet">'
        head += '<link href="../fontawesome/css/solid.css" rel="stylesheet">'

        # Google icons
        head += '<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">'
        
        # Goodies CSS
        head += '<!-- Computer Modern Serif-->'
        head += '<link rel="stylesheet" href="fonts/cmun-serif.css">\n'
        head += '<link rel="stylesheet" href="goodies.css" type="text/css">\n'

        head += '<script>'
        head += '$(document).ready(function(){'
        head += '$(".toast").toast();'
        head += '});'
        head += '</script>'


        # Google tracking
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

        head += '</head>\n'

        #enxerta no __body__ (top)
        body = '<body>\n\n'

        # body += '<div class="row">\n'

        body += '<div class=container-fluid>\n'
        body += '<div class=row>\n'
        body += '<div class=col-lg-1>\n'
        body += '</div>'
        body += '<div class=col-lg-10>\n\n'

        # general alert
        f = open('general_alert.html','r')
        body += f.read().replace('./politica.html','../politica.html')
        f.close()

        # colab alert
        f = open('colab_alert.html','r')
        aux = f.read().replace('./contato.html','../contato.html')
        aux = aux.replace('<span></span>',
                          '<span class="material-icons" style="font-size: 18px;">screen_rotation</span>')
        body += aux
        f.close()

        
        # Navbar
        body += '\n\n<!-- begin: navbar -->\n'
        body += '<nav class="navbar navbar-dark bg-primary mb-1">\n'
        body += '<div class="container-fluid">\n'
        body += '<a class="navbar-brand" href="main.html">Notas de Aula<br/><small>'+titulo_notas+'</small></a>\n'
        body += '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">\n'
        body += '<span class="navbar-toggler-icon"></span>\n'
        body += '</button>\n'
        body += '<div class="collapse navbar-collapse" id="navbarNav">\n'
        body += '<ul class="navbar-nav">\n'
        body += '<li class="nav-item"><a class="nav-link" href="../index.html"><i class="fas fa-home"></i> Início</a></li>\n'
        body += '<li class="nav-item"><a class="nav-link active" href="main.html">Sumário</a></li>\n'
        body += '<li class="nav-item"><a class="nav-link" href="main.pdf"><i class="fas fa-download" aria-hidden="true"></i> PDF</a></li>\n'
        body += '<li class="nav=item"><a class="nav-link" href="https://colab.research.google.com/github/phkonzen/notas/blob/master/notas.ipynb">Google Colab</a></li>\n'
        body += '<li class="nav-item dropdown">\n'
        body += '<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown">\n'
        body += 'Contato\n'
        body += '</a>\n'
        body += '<div class="dropdown-menu" aria-labelledby="navbarDropdown">\n'
        body += '<a class="dropdown-item" href="../contato.html"><i class="fas fa-envelope"></i> Mensagem</a>\n'
        body += '<a class="dropdown-item" href="https://www.instagram.com/notas.pedrok/"><i class="fab fa-instagram"></i> notas.pedrok</a>\n'
        body += '</div><!-- div class="dropdown-menu" aria-labelledby="navbarDropdown" -->\n'
        body += '</li> <!-- li class="nav-item dropdown" -->\n'
        body += '<li class="nav-item"><a class="nav-link" href="https://github.com/phkonzen/notas"><i class="fab fa-github" aria-hidden="true"></i> Repo</a></li>\n'
        body += '<li class="nav-item"><a class="nav-link" href="../politica.html">Política de dados</a></li>\n'
        body += '</ul>\n'
        body += '</div><!-- /.navbar-collapse -->\n'
        body += '</div><!-- /.container-fluid -->\n'
        body += '</nav>\n'
        body += '\n\n<!-- end: navbar -->\n\n\n'

        # redes sociais
        body += '<p class="text-left mb-0"><a href="./contato.html"><i class="fas fa-envelope"></i></a> | <a href="https://www.instagram.com/notas.pedrok/"><i class="fab fa-instagram"></i></a> | <a href="https://archive.org/details/notas-de-aula"><i class="fas fa-building-columns"></i></a> | <a href="https://www.youtube.com/channel/UCwutHKlKLgVj6IkFSUFBqoA"><i class="fab fa-youtube"></i></a> | <a href="https://github.com/phkonzen/notas"><i class="fab fa-github" aria-hidden="true"></i></a></p>\n\n\n'
        
        #enxerta no __body__ (bottom)
        body_end = ''

        # rodapé (id=rodape)
        f = open('rodape.html','r')
        rp = f.read()
        f.close()
        body_end += rp.replace('./contato.html','../contato.html')
        
        body_end += '</div> <!-- div class=col-lg-1 -->\n'
        body_end += '<div class=col-lg-1>\n'
        body_end += '</div>\n'
        body_end += '</div> <!-- div class=row -->\n'
        body_end += '</div> <!-- div class=container-fluid -->\n\n'

        body_end += '</body>\n'

        #enxerta no __footer__
        foot = '<div class="ltx_page_logo">\n'
        foot += '<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Licença Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a><br />O texto acima está sob Licença <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/deed.pt_BR">Creative Commons Atribuição-CompartilhaIgual 4.0 Internacional</a>. '

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

                #cria botões de link para contato
                if (fn != 'main'):
                    src_fname = fn
                    if (fn[0:4] == 'cap_'):
                        pos = fn.find('_sec')
                        if (pos != -1):
                            src_fname = fn[0:pos]

                    

                    link_to_src = ' <small><a href="../contato.html">'
                    link_to_src += '<i class="fas fa-envelope"></i></a></small>'

                    page = page.replace('</h1>',link_to_src+'</h1>')
                    page = page.replace('</h2>',link_to_src+'</h2>')

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
                            inc += '<ul class="list-group list-group-flush  d-inline-flex">\n'
                            if (yurl != "#"):
                                inc += '<a href="' + yurl + '" target=_blank' + \
                                    ' class="list-group-item list-group-item-action text-primary"><i class="fab fa-youtube fa-xl"></i> Assista no YouTube!</a>\n'
                            else:
                                inc += '<a href="#" class="list-group-item list-group-item-action list-group-item-light"><i class="fab fa-youtube fa-xl"></i> Assista no YouTube</a>\n'
                            

                            if (vurl != "#"):
                                inc += '<a href="' + vurl +  '" target=_blank' + \
                                    ' class="list-group-item list-group-item-action text-primary"><i class="fas fa-building-columns fa-xl"></i> Assista no archive.org!</a>\n'
                            else:
                                inc += '<a href="#" class="list-group-item list-group-item-action list-group-item-light"><i class="fas fa-building-columns fa-xl"></i> Assista no archive.org!</a>\n'
                                
                            if (aurl != "#"):
                                inc += '<a href="' + aurl +  '" target=_blank' + \
                                    ' class="list-group-item list-group-item-action text-primary"><i class="fas fa-file-audio fa-xl"></i> Escute a audioleitura!</a></a>\n'
                            else:
                                inc += '<a href="#" class="list-group-item list-group-item-action list-group-item-light"><i class="fas fa-file-audio fa-xl"></i> Escute a audioleitura!</a></a>\n'
                            
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
                            inc += '<ul class="list-group list-group-flush  d-inline-flex">\n'
                            if (yurl != "#"):
                                inc += '<a href="' + yurl +  '" target=_blank' + \
                                    ' class="list-group-item list-group-item-action text-primary"><i class="fab fa-youtube fa-xl"></i> Assista no YouTube!</a>\n'
                            else:
                                inc += '<a href="#" class="list-group-item list-group-item-action list-group-item-light"><i class="fab fa-youtube fa-xl"></i> Assista no YouTube</a>\n'
                            

                            if (vurl != "#"):
                                inc += '<a href="' + vurl +  '" target=_blank' + \
                                    ' class="list-group-item list-group-item-action text-primary"><i class="fas fa-building-columns fa-xl"></i> Assista no archive.org!</a>\n'
                            else:
                                inc += '<a href="#" class="list-group-item list-group-item-action list-group-item-light"><i class="fas fa-building-columns fa-xl"></i> Assista no archive.org!</a>\n'
                            
                            if (aurl != "#"):
                                inc += '<a href="' + aurl +  '" target=_blank' + \
                                    ' class="list-group-item list-group-item-action text-primary"><i class="fas fa-file-audio fa-xl"></i> Escute a audioleitura!</a></a>\n'
                            else:
                                inc += '<a href="#" class="list-group-item list-group-item-action list-group-item-light"><i class="fas fa-file-audio fa-xl"></i> Escute a audioleitura!</a></a>\n'
                            
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
                                '<button class="btn btn-info btn-sm" type="button" data-bs-toggle="collapse" '+ \
                                'data-bs-target="#'+respid+'">Resposta'+ \
                                '</button>'+ \
                                '\n<div class="collapse" id="'+respid+'">\n')
                    paux = page.find('ltx_theorem_resp')
                    
                #modifica o __footer__
                page = page.replace('<div class="ltx_page_logo">',foot)

                               
                #sobrescreve a página com as alterações
                f = open(htmldir+"/"+p,'w')
                f.write(page)
                f.close()
                        

        
