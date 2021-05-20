(TeX-add-style-hook
 "main"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("book" "12pt")))
   (TeX-run-style-hooks
    "latex2e"
    "../preambulo"
    "licenca"
    "prefacio"
    "./cap_numreal/cap_numreal"
    "./cap_funcao/cap_funcao"
    "./cap_respostas/cap_respostas"
    "book"
    "bk12")
   (LaTeX-add-bibliographies))
 :latex)

