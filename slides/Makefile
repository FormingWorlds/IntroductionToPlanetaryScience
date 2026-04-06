LECTURES = lecture01 lecture02 lecture03 lecture04 lecture05 lecture06 lecture07 lecture08
LATEXMK  = latexmk -xelatex -interaction=nonstopmode

.PHONY: all clean avif2png svg2pdf $(LECTURES)

all: $(LECTURES)

# Convert AVIF→PNG for XeLaTeX (figures + common assets)
avif2png:
	@echo "Converting AVIF → PNG for slides..."
	@find . -name '*.avif' -exec sh -c 'magick "$$1" "$${1%.avif}.png"' _ {} \;

# Convert SVG→PDF for XeLaTeX (vector figures)
# XeLaTeX cannot read SVG directly; cairosvg produces a PDF that xdvipdfmx can embed.
svg2pdf:
	@echo "Converting SVG → PDF for slides..."
	@find . -name '*.svg' -exec sh -c 'python3 -c "import cairosvg; cairosvg.svg2pdf(url=\"$$1\", write_to=\"$${1%.svg}.pdf\")"' _ {} \;

$(LECTURES): avif2png svg2pdf
	cd $@ && $(LATEXMK) $@.tex

clean:
	@for d in $(LECTURES); do \
		echo "Cleaning $$d ..."; \
		cd $$d && latexmk -C && cd ..; \
	done
	@find . -name '*.avif' -exec sh -c 'rm -f "$${1%.avif}.png"' _ {} \;
	@find . -name '*.svg' -exec sh -c 'rm -f "$${1%.svg}.pdf"' _ {} \;
