.PHONY: html pdf pdflatex slides worksheets minilectures clean avif2png gif2png

html:
	jupyter-book build book/

pdf:
	jupyter-book build book/ --builder pdfhtml

# Generate LaTeX, convert AVIF/GIF→PNG for XeLaTeX, then compile
pdflatex: avif2png gif2png
	jupyter-book build book/ --builder latex
	@find book/_build/latex/ -name '*.avif' -exec sh -c \
		'magick "$$1" "$${1%.avif}.png"' _ {} \;
	@find book/_build/latex/ -name '*.gif' -exec sh -c \
		'magick "$${1}[0]" "$${1%.gif}.png"' _ {} \;
	@sed -i '' -e 's/\.avif/.png/g' -e 's/\.gif/.png/g' book/_build/latex/*.tex
	cd book/_build/latex && make

# Convert AVIF→PNG beside originals for LaTeX builds
avif2png:
	@echo "Converting AVIF → PNG for LaTeX..."
	@find book/ -name '*.avif' ! -path '*/_build/*' -exec sh -c \
		'magick "$$1" "$${1%.avif}.png"' _ {} \;

# Extract first frame of any GIF as a PNG beside the original for LaTeX builds
gif2png:
	@echo "Extracting first frame of GIFs → PNG for LaTeX..."
	@find book/ -name '*.gif' ! -path '*/_build/*' -exec sh -c \
		'magick "$${1}[0]" "$${1%.gif}.png"' _ {} \;

slides:
	$(MAKE) -C slides

worksheets:
	$(MAKE) -C worksheets

minilectures:
	$(MAKE) -C minilectures

clean:
	jupyter-book clean book/
	@find book/ -name '*.avif' ! -path '*/_build/*' \
		-exec sh -c 'rm -f "$${1%.avif}.png"' _ {} \;
	@find book/ -name '*.gif' ! -path '*/_build/*' \
		-exec sh -c 'rm -f "$${1%.gif}.png"' _ {} \;
