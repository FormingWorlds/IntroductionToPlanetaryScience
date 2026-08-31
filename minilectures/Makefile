MINIS   = minilecture01 minilecture02 minilecture03 minilecture04 minilecture05 minilecture06
LATEXMK = latexmk -xelatex -interaction=nonstopmode

.PHONY: all clean web assets $(MINIS)

all: $(MINIS)

# The decks borrow theme assets and title backgrounds from slides/; convert
# AVIF/SVG sources there before compiling.
assets:
	$(MAKE) -C ../slides avif2png svg2pdf

$(MINIS): assets
	cd $@ && $(LATEXMK) $@.tex

# Web-distribution target: ghostscript-flatten each deck into
# ../book/_static/minilectures/, same recipe as the lecture slides.
WEB_OUT = ../book/_static/minilectures
web: $(MINIS)
	@mkdir -p $(WEB_OUT)
	@for n in $(MINIS); do \
	  echo "Outlining $$n -> $(WEB_OUT)/$$n.pdf"; \
	  gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/ebook \
	     -dColorImageResolution=300 -dGrayImageResolution=300 \
	     -dMonoImageResolution=600 -dNoOutputFonts \
	     -dNOPAUSE -dBATCH -dQUIET \
	     -sOutputFile=$(WEB_OUT)/$$n.pdf $$n/$$n.pdf; \
	done

clean:
	@for d in $(MINIS); do \
		echo "Cleaning $$d ..."; \
		cd $$d && latexmk -C && cd ..; \
	done
