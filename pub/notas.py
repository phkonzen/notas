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
        text += 'font-size: 101%;\n'
        text += '}\n\n'
        
        text += '.navbar {\n'
        text += 'height: auto;\n'
        text += 'padding: 5px;\n'
        text += '}\n\n'

        if (srcref != 'MatematicaNumericaParalela'):
            text += '.ltx_lst_numbers_left .ltx_listingline .ltx_tag {\n'
            text += 'margin-left:-1em; width:2.5em;\n'
            text += 'text-align:right; }\n'
        
        f.write(text)
        f.close()
        
        #enxerta no __head__
        head = ''
        
        head += '<meta name="author" content="Pedro H A Konzen"/>\n'
        head += '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n'

        #BootstrapCDN v.4.5
        head += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">\n'
        head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>\n'
        head += '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>\n'
        head += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>\n'

        # FontAwesome
        head += '<script src="https://kit.fontawesome.com/dfbff2c7ed.js" crossorigin="anonymous"></script>'

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
        head += '\n<!-- Global site tag (gtag.js) - Google Analytics -->\n'
        head += '<script async src="https://www.googletagmanager.com/gtag/js?id=UA-17226092-2"></script>\n'
        head += '<script>\n'
        head += 'window.dataLayer = window.dataLayer || [];\n'
        head += 'function gtag(){dataLayer.push(arguments);}\n'
        head += 'gtag("js", new Date());\n'
        head += '\ngtag("config", "UA-17226092-2")\n';
        head += '</script>\n'

        head += '<script>\n'
        head += '$(document).ready(function () {\n'
        head += '$("#colabAlert").hide();\n'
        head += '$("#generalAlert").hide();\n'
        head += 'if (document.referrer.lastIndexOf("://phkonzen.github.io/notas/") == -1) {\n'
        head += '$("#generalAlert").fadeIn(100);\n'
        head += '}\n'
        head += '$("#colabAlert").delay(3000).fadeIn(100);\n'
        head += '});\n'    
        head += '</script>\n\n'

        head += '</head>\n'

        #enxerta no __body__ (top)
        body = '<body>\n\n'

        # body += '<div class="row">\n'

        body += '<div class=container-fluid>\n'
        body += '<div class=row>\n'
        body += '<div class=col-lg-1>\n'
        body += '</div>'
        body += '<div class=col-lg-10>\n\n'
      
        # Navbar
        body += '\n\n<!-- begin: navbar -->\n'
        body += '<nav class="navbar navbar-expand-lg navbar-light bg-light">\n'
        body += '<a class="navbar-brand" href="main.html">Notas de Aula<br/><small>'+titulo_notas+'</small></a>\n'
        body += '<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">\n'
        body += '<span class="navbar-toggler-icon"></span>\n'
        body += '</button>\n'
        body += '<div class="collapse navbar-collapse" id="navbarNav">\n'
        body += '<ul class="navbar-nav">\n'
        body += '<li class="nav-item"><a class="nav-link" href="../index.html"><i class="fas fa-home"></i> Início</a></li>\n'
        body += '<li class="nav-item active"><a class="nav-link" href="main.html">Sumário</a></li>\n'
        body += '<li class="nav-item"><a class="nav-link" href="main.pdf"><i class="fa fa-download" aria-hidden="true"></i> PDF</a></li>\n'
        body += '<li class="nav=item"><a class="nav-link" href="https://mybinder.org/v2/gh/phkonzen/notas/master?filepath=notas.ipynb">Jupyter NB</a></li>\n'
        body += '<li class="nav-item dropdown">\n'
        body += '<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n'
        body += 'Contato\n'
        body += '</a>\n'
        body += '<div class="dropdown-menu" aria-labelledby="navbarDropdown">\n'
        body += '<a class="dropdown-item" href="../contato.html"><i class="fas fa-envelope"></i> Mensagem</a>\n'
        body += '<a class="dropdown-item" href="https://www.instagram.com/notas.pedrok/"><i class="fab fa-instagram"></i> notas.pedrok</a>\n'
        body += '</div><!-- div class="dropdown-menu" aria-labelledby="navbarDropdown" -->\n'
        body += '</li> <!-- li class="nav-item dropdown" -->\n'
        body += '<li class="nav-item"><a class="nav-link" href="https://github.com/phkonzen/notas"><i class="fa fa-github" aria-hidden="true"></i> Repo</a></li>\n'
        body += '<li class="nav-item"><a class="nav-link" href="../politica.html">Política de dados</a></li>\n'
        body += '</ul>\n'
        body += '</div><!-- /.navbar-collapse -->\n'
        body += '</nav>\n'
        body += '\n\n<!-- end: navbar -->\n\n\n'

       
        #enxerta no __body__ (bottom)
        body_end = ''

        # rodapé (id=rodape)
        f = open('rodape.html','r')
        rp = f.read()
        f.close()
        body_end += rp.replace('./contato.html','../contato.html')

        # colab alert
        f = open('colab_alert.html','r')
        ga = f.read()
        f.close()
        # ga = ga.replace('font-size:0.9em','font-size:0.85em')
        body_end += ga.replace('./contato.html','../contato.html')

        # general alert
        f = open('general_alert.html','r')
        ga = f.read()
        f.close()
        # ga = ga.replace('font-size:0.9em','font-size:0.85em')
        body_end += ga.replace('./politica.html','../politica.html')

        
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

                    # mídia
                    i1 = page.find('[Vídeo]')
                    while (i1 != -1):
                        vurl = ''
                        aurl = ''
                        # vídeo URL
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
                        # page = page[0:i2] + \
                        #     '<!-- mídia -->' + \
                        #     page[f2+6:len(page)]

                        f3 = page.index('right',i2)
                        inc = '' # page[i2:f3] + 'left">\n'
                        if (aurl != ''):
                            # inc += '<p class="ltx_p">\n'
                            aurl = aurl.replace('/details/','/embed/')
                            inc += '<iframe src="' + \
                                aurl + \
                                '" width="500" height="30" style="max-width:100%;" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe>\n'
                            inc += '<p class="ltx_p"></p>\n'
                            
                        if (vurl != ''):
                            vurl = vurl.replace('/details/','/embed/')
                            inc += '<div class="row">\n'
                            inc += '<div class="col-xl-4 col-lg-3 col-md-3"></div>\n'
                            inc += '<div class="col-xl-4 col-lg-6 col-md-6">\n'
                            inc += '<div class="container" style="position:relative; width:100%; padding-top:75%; background-color:black;">\n'
                            inc += '<iframe src="' + \
                                vurl + \
                                '" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" style="display:block; position:absolute; width:100%; height:100%; left:0; right:0; top:0; bottom:0;" allowfullscreen></iframe>\n'
                            inc += '</div>\n'
                            inc += '</div>\n'
                            inc += '</div>\n'

                        page = page[0:i2] + \
                            inc + \
                            page[f2+6:len(page)]
                            
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
                                '<small><button data-toggle="collapse" '+ \
                                'data-target="#'+respid+'">Resp.'+ \
                                '</button></small>'+ \
                                '\n<div id="'+respid+'" class="collapse">\n')
                    paux = page.find('ltx_theorem_resp')
                    
                #modifica o __footer__
                page = page.replace('<div class="ltx_page_logo">',foot)

                               
                #sobrescreve a página com as alterações
                f = open(htmldir+"/"+p,'w')
                f.write(page)
                f.close()
                        

        
