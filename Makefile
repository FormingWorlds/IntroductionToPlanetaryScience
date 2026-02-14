.PHONY: html pdf pdflatex clean

html:
	jupyter-book build book/

pdf:
	jupyter-book build book/ --builder pdfhtml

pdflatex:
	jupyter-book build book/ --builder pdflatex

clean:
	jupyter-book clean book/
