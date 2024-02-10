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
# FORMATO HTML
########################################

html: main.tex
	cp ../config-html.knd config.knd
	rm -rvf ./html
	mkdir -p ./html
	cp -rvf ../fonts html/
	latexmlc main.tex \
        --splitat=section -splitnaming=label \
		--includestyles \
		--css="./fonts/cmun-serif.css" \
		--format=html \
		--javascript='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=MML_SVG' \
		--dest=html/main.html -
	cp ../config-book.knd config.knd

########################################
# FORMATO EPUB
########################################

epub: main.tex
	cp ../notas.css . 
	latexmlc main.tex \
			 --dest=main.epub \
			 --includestyles \
			 --css=notas.css


########################################
# TODOS AS VERSÕES EM FORMATO PDF
########################################

all: main.tex
	make clean
	make pdf
	make clean
	make html
	make clean
	make epub


.PHONY: clean

clean:
	rm -rvf *.aux */*.aux *.log *.out *.toc *.bbl */*.bbl \
	      	*.idx *.ilg *.ind *.blg *.backup \
	      	*.4tc *.lg *.tmp *.xref *.png *.html \
	      	*.4ct *.css *.idv *.maf *.mtc *.mtc0 \
	      	*.xml html *.pdf *.dvi *.js x.tex
