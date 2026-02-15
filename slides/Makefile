LECTURES = lecture01
LATEXMK  = latexmk -xelatex -interaction=nonstopmode

.PHONY: all clean $(LECTURES)

all: $(LECTURES)

$(LECTURES):
	cd $@ && $(LATEXMK) $@.tex

clean:
	@for d in $(LECTURES); do \
		echo "Cleaning $$d ..."; \
		cd $$d && latexmk -C && cd ..; \
	done
