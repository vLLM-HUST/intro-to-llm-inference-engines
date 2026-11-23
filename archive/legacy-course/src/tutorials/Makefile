MD_DIR := md
OUT_DIR := ../../build/tutorials
PANDOC ?= pandoc
PDF_ENGINE ?= tectonic
LUA_FILTER := pandoc/question_space.lua
MD_FILES := $(wildcard $(MD_DIR)/Tutorial_*.md)
PDF_TARGETS := $(patsubst $(MD_DIR)/%.md,$(OUT_DIR)/%.pdf,$(MD_FILES))

.PHONY: all list clean

all: $(PDF_TARGETS)

list:
	@printf '%s\n' $(MD_FILES)

$(OUT_DIR)/%.pdf: $(MD_DIR)/%.md
	@mkdir -p "$(OUT_DIR)"
	@$(PANDOC) "$<" \
		--from markdown+raw_tex \
		--lua-filter=$(LUA_FILTER) \
		--pdf-engine=$(PDF_ENGINE) \
		-V documentclass=ctexart \
		-V geometry:margin=2.2cm \
		-V colorlinks=true \
		-V urlcolor=blue \
		-V papersize=a4 \
		-o "$@"

clean:
	@find $(OUT_DIR) -maxdepth 1 -type f -name 'Tutorial_*.pdf' -delete 2>/dev/null || true
