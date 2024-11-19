main: main.tex
	mkdir -p ./html
	rm -rvf ./html/*	
	latexmlc main.tex \
						--format=html5 --pmml \
						--javascript=LaTeXML-maybeMathJax.js \
						--dest=html/main.html -
