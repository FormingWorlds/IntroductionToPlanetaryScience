LECTURES = lecture01
LATEXMK  = latexmk -xelatex -interaction=nonstopmode

.PHONY: all clean avif2png $(LECTURES)

all: $(LECTURES)

# Convert AVIF→PNG for XeLaTeX (figures + common assets)
avif2png:
	@echo "Converting AVIF → PNG for slides..."
	@find . -name '*.avif' -exec sh -c 'magick "$$1" "$${1%.avif}.png"' _ {} \;

$(LECTURES): avif2png
	cd $@ && $(LATEXMK) $@.tex

clean:
	@for d in $(LECTURES); do \
		echo "Cleaning $$d ..."; \
		cd $$d && latexmk -C && cd ..; \
	done
	@find . -name '*.avif' -exec sh -c 'rm -f "$${1%.avif}.png"' _ {} \;
