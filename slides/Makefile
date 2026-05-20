TEX_DIR := tex
OUT_DIR := .
TECTONIC ?= tectonic
TEX_FILES := $(filter-out $(TEX_DIR)/大模型推理基础设施_课件样式.tex,$(wildcard $(TEX_DIR)/*.tex))
PDF_TARGETS := $(patsubst $(TEX_DIR)/%.tex,$(OUT_DIR)/%.pdf,$(TEX_FILES))

.PHONY: all list clean

all: $(PDF_TARGETS)

list:
	@printf '%s\n' $(TEX_FILES)

$(OUT_DIR)/%.pdf: $(TEX_DIR)/%.tex
	@cd $(TEX_DIR) && $(TECTONIC) --outdir ../$(OUT_DIR) "$*.tex"

clean:
	@find $(OUT_DIR) -maxdepth 1 -type f \( -name '*.aux' -o -name '*.log' -o -name '*.nav' -o -name '*.out' -o -name '*.snm' -o -name '*.toc' -o -name '*.xdv' -o -name '*.fls' -o -name '*.fdb_latexmk' -o -name '*.synctex.gz' \) -delete
