LECTURES = lecture01 lecture02 lecture03 lecture04 lecture05 lecture06 lecture07 lecture08 lecture09 lecture10 lecture11 lecture12 lecture13 lecture14
LATEXMK  = latexmk -xelatex -interaction=nonstopmode

.PHONY: all clean avif2png svg2pdf web $(LECTURES)

all: $(LECTURES)

# Web-distribution target: build all decks, then ghostscript-flatten each one
# into ../book/_static/slides/lectureNN.pdf. Text is converted to vector paths
# (-dNoOutputFonts) so macOS Preview and other PDF viewers cannot mis-render
# embedded OpenType fonts. Images kept at 300 dpi colour and 600 dpi mono so
# schematic-figure labels stay legible (the /ebook default of 150 dpi blurred
# them too much for some figures). Final files are 3-6 MB each, total ~45 MB.
WEB_OUT = ../book/_static/slides
web: $(LECTURES)
	@mkdir -p $(WEB_OUT)
	@for n in $(LECTURES); do \
	  echo "Outlining $$n -> $(WEB_OUT)/$$n.pdf"; \
	  gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/ebook \
	     -dColorImageResolution=300 -dGrayImageResolution=300 \
	     -dMonoImageResolution=600 -dNoOutputFonts \
	     -dNOPAUSE -dBATCH -dQUIET \
	     -sOutputFile=$(WEB_OUT)/$$n.pdf $$n/$$n.pdf; \
	done

# Convert AVIF→PNG for XeLaTeX (figures + common assets)
# Force 8-bit sRGB without alpha: xdvipdfmx silently drops 16-bit and graya PNGs
avif2png:
	@echo "Converting AVIF → PNG for slides..."
	@rm -f .conv_failed
	@find . -name '*.avif' -exec sh -c 'out="$${1%.avif}.png"; err=$$(magick "$$1" -depth 8 -alpha remove -alpha off -colorspace sRGB -type TrueColor "$$out" 2>&1); file "$$out" 2>/dev/null | grep -q "PNG image" || ffmpeg -v error -y -i "$$1" -pix_fmt rgb24 "$$out" || { printf "avif2png: magick and ffmpeg both failed for %s\nmagick said: %s\n" "$$1" "$$err" >&2; touch .conv_failed; }' _ {} \;
	@test ! -f .conv_failed

# Convert SVG→PDF for XeLaTeX (vector figures)
# XeLaTeX cannot read SVG directly; cairosvg produces a PDF that xdvipdfmx can embed.
svg2pdf:
	@echo "Converting SVG → PDF for slides..."
	@rm -f .conv_failed
	@find . -name '*.svg' -exec sh -c 'out="$${1%.svg}.pdf"; python3 -c "import cairosvg; cairosvg.svg2pdf(url=\"$$1\", write_to=\"$$out\")" 2>/dev/null || rsvg-convert -f pdf -o "$$out" "$$1" || { echo "svg2pdf: cairosvg and rsvg-convert both failed for $$1" >&2; touch .conv_failed; }' _ {} \;
	@test ! -f .conv_failed

$(LECTURES): avif2png svg2pdf
	cd $@ && $(LATEXMK) $@.tex

clean:
	@for d in $(LECTURES); do \
		echo "Cleaning $$d ..."; \
		cd $$d && latexmk -C && cd ..; \
	done
	@find . -name '*.avif' -exec sh -c 'rm -f "$${1%.avif}.png"' _ {} \;
	@find . -name '*.svg' -exec sh -c 'rm -f "$${1%.svg}.pdf"' _ {} \;
