#Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

########################################
# FORMATO LIVRO PDF
########################################

pdf: main.tex
	rm -f main.aux
	cp config-book.knd config.knd
	pdflatex main
	bibtex main
	makeindex main
	pdflatex main
	pdflatex main


########################################
# FORMATO LIVRO DVI
########################################

dvi: main.tex
	cp config-book.knd config.knd
	latex main
	bibtex main
	makeindex main
	latex main
	latex main
	cp config-book.knd config.knd


########################################
# FORMATO HTML
########################################

html: main.html

main.html: main.tex
	cp config-html.knd config.knd
	rm -rvf ./html
	mkdir -p ./html
	cp -rvf ../fonts html/
	latexml main.tex | latexmlpost \
        --splitat=section -splitnaming=label \
	--css=../main.css \
	--format=html \
	--javascript='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=MML_SVG' \
	--javascript=../mymathcfg.js \
	--dest=html/main.html -
	cp config-book.knd config.knd

########################################
# TODOS AS VERSÕES EM FORMATO PDF
########################################

all: main.tex
	make clean
	make pdf
	make clean
	make dvi
	make clean
	make html


.PHONY: clean

clean:
	rm -rvf *.aux */*.aux *.log *.out *.toc *.bbl */*.bbl \
	      	*.idx *.ilg *.ind *.blg *.backup \
	      	*.4tc *.lg *.tmp *.xref *.png *.html \
	      	*.4ct *.css *.idv *.maf *.mtc *.mtc0 \
	      	*.xml html *.pdf *.dvi *.js
