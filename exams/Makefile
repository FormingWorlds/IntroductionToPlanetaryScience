DOCS    = formulalist
LATEXMK = latexmk -xelatex -interaction=nonstopmode

.PHONY: all clean web $(DOCS)

all: $(DOCS)

$(DOCS):
	cd $@ && $(LATEXMK) $@.tex

# Web-distribution target: copy the built PDFs to the Jupyter Book static tree.
WEB_OUT = ../book/_static/exams
web: $(DOCS)
	@mkdir -p $(WEB_OUT)
	@for n in $(DOCS); do \
	  cp $$n/$$n.pdf $(WEB_OUT)/$$n.pdf; \
	  echo "Published $$n -> $(WEB_OUT)"; \
	done

clean:
	@for d in $(DOCS); do \
		echo "Cleaning $$d ..."; \
		cd $$d && latexmk -C && cd ..; \
	done
