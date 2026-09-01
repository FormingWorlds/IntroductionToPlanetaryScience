DOCS    = formulalist
EXAMS   = mockexam01 mockexam02 mockexam03
LATEXMK = latexmk -xelatex -interaction=nonstopmode

.PHONY: all clean web $(DOCS) $(EXAMS)

all: $(DOCS) $(EXAMS)

$(DOCS):
	cd $@ && $(LATEXMK) $@.tex

# Each exam builds twice from one content file: the problem sheet and the
# solution sheet. Both are published, so both are built by default.
$(EXAMS):
	cd $@ && $(LATEXMK) $@.tex && $(LATEXMK) $@_solutions.tex

# Web-distribution target: copy the built PDFs to the Jupyter Book static tree.
WEB_OUT = ../book/_static/exams
web: $(DOCS) $(EXAMS)
	@mkdir -p $(WEB_OUT)
	@for n in $(DOCS); do \
	  cp $$n/$$n.pdf $(WEB_OUT)/$$n.pdf && \
	  echo "Published $$n -> $(WEB_OUT)" || exit 1; \
	done
	@for n in $(EXAMS); do \
	  cp $$n/$$n.pdf $(WEB_OUT)/$$n.pdf && \
	  cp $$n/$${n}_solutions.pdf $(WEB_OUT)/$${n}_solutions.pdf && \
	  echo "Published $$n -> $(WEB_OUT)" || exit 1; \
	done

clean:
	@for d in $(DOCS) $(EXAMS); do \
		echo "Cleaning $$d ..."; \
		(cd $$d && latexmk -C); \
	done
