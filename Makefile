SRC          := $(wildcard src/*.md)
TARGETS_HTML := $(patsubst src/%.md,_build/html/%.html,$(SRC))
TARGETS_EPUB := $(patsubst src/%.md,_build/epub/%.epub,$(SRC))
TARGETS_PDF  := $(patsubst src/%.md,_build/pdf/%.pdf,$(SRC))
TARGETS      := $(TARGETS_HTML) $(TARGETS_EPUB) $(TARGETS_PDF)

all: $(TARGETS)

_build/html/%.html: src/%.md
	mkdir -p _build/html
	pandoc --self-contained -s -o $@ --resource-path src/ --highlight-style pygments --columns 1000 --css assets/td.css --ascii --number-sections --mathml $^

_build/epub/%.epub: src/%.md
	mkdir -p _build/epub
	pandoc -o $@ --resource-path src/ --columns 1000 --number-sections --css assets/td_epub.css --mathml $^

_build/pdf/%.pdf: src/%.md
	mkdir -p _build/pdf
	pandoc -V lang=fr -o $@ --resource-path src/ --template assets/custom-eisvogel.tex --listings --columns 1000 --variable urlcolor=cyan --number-sections $^

clean:
	rm -f $(TARGETS)
