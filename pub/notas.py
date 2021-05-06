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
        
        f.write(text)
        f.close()
        
        #enxerta no __head__
        head = ''
        
        head += '<meta name="author" content="Pedro H A Konzen"/>\n'
        head += '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n'

        # # BootstrapCDN v.3.3
        # head += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n'
        # head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n'
        # head += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\n'

        #BootstrapCDN v.4.5
        # head += '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">\n'
        head += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">\n'
        head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>\n'
        head += '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>\n'
        head += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>\n'

        # FontAwesome
        head += '<script src="https://kit.fontawesome.com/dfbff2c7ed.js" crossorigin="anonymous"></script>'

        # Goodies CSS
        head += '<!-- Computer Modern Serif-->'
        head += '<link rel="stylesheet" href="fonts/cmun-serif.css"></link>'
        head += '<link rel="stylesheet" href="goodies.css" type="text/css">\n'

        # head += '\n\n'
        # head+= '<!-- JavaScript -->\n'
        # head += '<!-- jQuery first, then Popper.js, then Bootstrap JS -->\n'
        # head += '<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>\n'
        # head += '<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>\n'
        # head += '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>\n\n'

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
        head += '$("#colabAlert").delay(2000).fadeIn(100);\n'  
        head += '});\n'    
        head += '</script>\n\n'

        head += '<script>\n'
        head += '$(document).ready(function () {\n'
        head += '$("#colabAlert").hide();\n'
        head += '$("#generalAlert").hide();\n'
        head += 'if (document.referrer.lastIndexOf("://phkonzen.github.io/notas") != 0) {\n'
        head += '$("#generalAlert").fadeIn(0);\n'
        head += '}\n'
        head += '$("#colabAlert").delay(2000).fadeIn(100);\n'
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
        body += '<nav class="navbar navbar-expand-md navbar-light bg-light">\n'
        body += '<a class="navbar-brand" href="main.html">Notas de Aula<br/><small>'+titulo_notas+'</small></a>\n'
        body += '<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">\n'
        body += '<span class="navbar-toggler-icon"></span>\n'
        body += '</button>\n'
        body += '<div class="collapse navbar-collapse" id="navbarNav">\n'
        body += '<ul class="navbar-nav">\n'
        body += '<li class="nav-item active"><a class="nav-link" href="main.html">Sumário</a></li>\n'
        body += '<li class="nav-item"><a class="nav-link" href="https://github.com/phkonzen/notas"><i class="fa fa-github" aria-hidden="true"></i> Repo</a></li>\n'
        body += '<li class="nav-item"><a class="nav-link" href="main.pdf"><i class="fa fa-download" aria-hidden="true"></i> PDF</a></li>\n'
        body += '<li class="nav=item"><a class="nav-link" href="https://mybinder.org/v2/gh/phkonzen/notas/master?filepath=notas.ipynb" target="_blank">Jupyter NB</a></li>\n'
        body += '<li class="nav-item"><a class="nav-link" href="../index.html">Outras Notas & Infos</a></li>\n'
        body += '</ul>\n'
        body += '</div><!-- /.navbar-collapse -->\n'
        body += '</nav>\n'
        body += '\n\n<!-- end: navbar -->\n\n\n'

       
        #enxerta no __body__ (bottom)
        body_end = ''

        # # botão flutuante fixo 
        # body_end += '<div class="toast fade show" aria-live="polite" style="position: fixed; bottom: 0">'
        # body_end += '<div class="toast-header">'
        # body_end += '<strong class="mr-auto"><a href="../contato.html" target="_blank"><i class="fas fa-envelope"></i> Erros? Sugestões? </a></strong>'
        # body_end += '<button type="button" class="ml-2 mb-1 close" data-dismiss="toast">&times;</button>'
        # body_end += '</div>'
        # body_end += '<div class="toast-body">'
        # body_end += '<a href="../contato.html" target="_blank">Clique aqui para informar erros ou deixar sujestões!</a>'
        # body_end += '</div>'
        # body_end += '</div>'

        body_end += '<div class="card" style="font-size:0.9em">\n'
        body_end += '<div class="card-footer text-left">\n'
        body_end += '<i class="fa fa-github" aria-hidden="true"></i> GitHub Repo: '
        body_end += '<a href="https://github.com/phkonzen/notas" target="_blank">https://github.com/phkonzen/notas</a>. Contato '
        body_end += '<a href="contato.html" target="_blank"><i class="fas fa-envelope"></i></a>\n'
        body_end += '</div> <!-- div class="card" -->\n'
        body_end += '</div> <!-- div class="card-footer text-right" -->\n'


        # # alerta de colaboração
        # body_end += '<div class="alert alert-warning alert-dismissible" role="alert" style="position: fixed; bottom: 0; font-size:0.85em;">\n'
        # body_end += '<span type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></span>\n'
        # body_end += '<a href="../contato.html">Clique <strong>aqui</strong> para <strong>informar</strong> <span style="color:red"><strong>erros</strong></span> ou dar <span style="color:red"><strong>sugestões</strong></span>!</a>'
        # body_end += '</div>\n\n'

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

                    

                    link_to_src = ' <small><a href="../contato.html" target="_blank">'
                    link_to_src += '<i class="fas fa-envelope"></i></a></small>'

                    page = page.replace('</h1>',link_to_src+'</h1>')
                    page = page.replace('</h2>',link_to_src+'</h2>')

                    # # vídeo icon
                    # page = page.replace('[Vídeo]','<i class="fas fa-film"></i>')
                    # # áudio icon
                    # page = page.replace('[Áudio]','<i class="fas fa-music"></i>')

                    # #cria formulário de contato
                    # f = open("contato.html",'r')
                    # tcon = f.read()
                    # f.close()

                    # tcon = tcon.replace('+++fromurl+++',srcref+'/'+p)

                    # f = open(htmldir+'/contato_'+p,'w')
                    # f.write(tcon)
                    # f.close()

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
                        

        
