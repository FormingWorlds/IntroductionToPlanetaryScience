SHEETS  = worksheet01 worksheet02 worksheet03 worksheet04 worksheet05 worksheet06
LATEXMK = latexmk -xelatex -interaction=nonstopmode

.PHONY: all clean web $(SHEETS)

all: $(SHEETS)

# Each sheet builds twice from one content file: the problem sheet and the
# solution sheet. Both are published, so both are built by default.
$(SHEETS):
	cd $@ && $(LATEXMK) $@.tex && $(LATEXMK) $@_solutions.tex

# Web-distribution target: copy the built PDFs to the Jupyter Book static tree.
WEB_OUT = ../book/_static/worksheets
web: $(SHEETS)
	@mkdir -p $(WEB_OUT)
	@for n in $(SHEETS); do \
	  cp $$n/$$n.pdf $(WEB_OUT)/$$n.pdf; \
	  cp $$n/$${n}_solutions.pdf $(WEB_OUT)/$${n}_solutions.pdf; \
	  echo "Published $$n -> $(WEB_OUT)"; \
	done

clean:
	@for d in $(SHEETS); do \
		echo "Cleaning $$d ..."; \
		cd $$d && latexmk -C && cd ..; \
	done
