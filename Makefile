.PHONY: html pdf pdflatex slides clean

html:
	jupyter-book build book/

pdf:
	jupyter-book build book/ --builder pdfhtml

pdflatex:
	jupyter-book build book/ --builder pdflatex

slides:
	$(MAKE) -C slides

clean:
	jupyter-book clean book/
