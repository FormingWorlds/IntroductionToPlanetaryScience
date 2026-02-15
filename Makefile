.PHONY: html pdf pdflatex slides clean avif2png

html:
	jupyter-book build book/

pdf:
	jupyter-book build book/ --builder pdfhtml

# Generate LaTeX, convert AVIF→PNG for XeLaTeX, then compile
pdflatex: avif2png
	jupyter-book build book/ --builder latex
	@find book/_build/latex/ -name '*.avif' -exec sh -c \
		'magick "$$1" "$${1%.avif}.png"' _ {} \;
	@sed -i '' 's/\.avif/.png/g' book/_build/latex/*.tex
	cd book/_build/latex && make

# Convert AVIF→PNG beside originals for LaTeX builds
avif2png:
	@echo "Converting AVIF → PNG for LaTeX..."
	@find book/ -name '*.avif' ! -path '*/_build/*' -exec sh -c \
		'magick "$$1" "$${1%.avif}.png"' _ {} \;

slides:
	$(MAKE) -C slides

clean:
	jupyter-book clean book/
	@find book/ -name '*.avif' ! -path '*/_build/*' \
		-exec sh -c 'rm -f "$${1%.avif}.png"' _ {} \;
