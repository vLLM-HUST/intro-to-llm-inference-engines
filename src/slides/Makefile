TEX_DIR := tex
TECTONIC ?= tectonic
ROOT_DIR := ../..
LECTURE_OUT_DIR := $(ROOT_DIR)/build/slides/lectures
HANDOUT_OUT_DIR := $(ROOT_DIR)/build/slides/handouts
STYLE_FILE := $(TEX_DIR)/大模型推理基础设施_课件样式.tex
HANDOUT_FILE := $(TEX_DIR)/大模型推理基础设施_课程导论讲义.tex
LECTURE_TEX_FILES := $(filter-out $(STYLE_FILE) $(HANDOUT_FILE),$(wildcard $(TEX_DIR)/*.tex))
HANDOUT_TEX_FILES := $(HANDOUT_FILE)
LECTURE_PDF_TARGETS := $(patsubst $(TEX_DIR)/%.tex,$(LECTURE_OUT_DIR)/%.pdf,$(LECTURE_TEX_FILES))
HANDOUT_PDF_TARGETS := $(patsubst $(TEX_DIR)/%.tex,$(HANDOUT_OUT_DIR)/%.pdf,$(HANDOUT_TEX_FILES))
PDF_TARGETS := $(LECTURE_PDF_TARGETS) $(HANDOUT_PDF_TARGETS)

.PHONY: all list clean

all: $(PDF_TARGETS)

list:
	@printf '%s\n' $(LECTURE_TEX_FILES) $(HANDOUT_TEX_FILES)

$(LECTURE_OUT_DIR)/%.pdf: $(TEX_DIR)/%.tex
	@mkdir -p "$(LECTURE_OUT_DIR)"
	@cd $(TEX_DIR) && $(TECTONIC) --outdir "$(abspath $(LECTURE_OUT_DIR))" "$*.tex"

$(HANDOUT_OUT_DIR)/%.pdf: $(TEX_DIR)/%.tex
	@mkdir -p "$(HANDOUT_OUT_DIR)"
	@cd $(TEX_DIR) && $(TECTONIC) --outdir "$(abspath $(HANDOUT_OUT_DIR))" "$*.tex"

clean:
	@find $(LECTURE_OUT_DIR) $(HANDOUT_OUT_DIR) -type f -name '*.pdf' -delete 2>/dev/null || true
	@find . -maxdepth 1 -type f \( -name '*.aux' -o -name '*.log' -o -name '*.nav' -o -name '*.out' -o -name '*.snm' -o -name '*.toc' -o -name '*.xdv' -o -name '*.fls' -o -name '*.fdb_latexmk' -o -name '*.synctex.gz' \) -delete
