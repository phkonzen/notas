#Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

########################################
# FORMATO LIVRO PDF
########################################

pdf: main.tex
	cp ../config-book.knd config.knd
	pdflatex main
	pdflatex main
	pdflatex main

########################################
# FORMATO LIVRO PDF (Draft)
########################################

pdf-draft: main.tex
	cp ../config-book-draft.knd config.knd
	pdflatex main
	pdflatex main
	pdflatex main


########################################
# FORMATO HTML
########################################

html: main.tex
	cp ../config-html.knd config.knd
	rm -rvf ./html
	mkdir -p ./html
	cp -rvf ../fonts html/
	cp ../notas.css html/
	latexmlc main.tex \
    --splitat=section --splitnaming=label \
		--includestyles \
		--css="./fonts/cmun-serif.css" \
		--css="./notas.css" \
		--format=html5 \
		--pmml \
		--javascript='https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js' \
		--linelength=25 \
		--dest=html/main.html -
	cp ../config-book.knd config.knd


########################################
# TODOS AS VERSÕES
########################################

all: main.tex
	make clean
	make pdf
	make clean
	make html


.PHONY: clean

clean:
	rm -rvf *.aux */*.aux *.log *.out *.toc *.bbl */*.bbl \
	      	*.idx *.ilg *.ind *.blg *.backup \
	      	*.4tc *.lg *.tmp *.xref *.png *.html \
	      	*.4ct *.css *.idv *.maf *.mtc *.mtc0 \
	      	*.xml html *.pdf *.dvi *.js x.tex
