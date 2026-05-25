PANDOC ?= pandoc
PDF_ENGINE ?= tectonic
HEADER_FILE := pandoc/experiment-sheet-header.tex
OUT_DIR := ../../../build/experiments/nano-vLLM实验课
SHEET_DIRS := experiment_1_最小运行与代码地图 \
	experiment_2_请求生命周期观察 \
	experiment_3_调度与连续批处理实验 \
	experiment_4_KV状态与缓存组织实验 \
	experiment_5_指标观测与最小复现实验 \
	project_课程项目实验说明
MD_FILES := $(addsuffix /sheet.md,$(SHEET_DIRS))
PDF_TARGETS := $(addprefix $(OUT_DIR)/,$(addsuffix /sheet.pdf,$(SHEET_DIRS)))

.PHONY: all list clean

all: $(PDF_TARGETS)

list:
	@printf '%s\n' $(MD_FILES)

$(OUT_DIR)/%/sheet.pdf: %/sheet.md $(HEADER_FILE)
	@mkdir -p "$(dir $@)"
	@$(PANDOC) "$<" \
		--from markdown+raw_tex \
		--include-in-header=$(HEADER_FILE) \
		--pdf-engine=$(PDF_ENGINE) \
		-V documentclass=ctexart \
		-V geometry:margin=2.2cm \
		-V colorlinks=true \
		-V urlcolor=blue \
		-V papersize=a4 \
		-o "$@"

clean:
	@find $(OUT_DIR) -type f -name 'sheet.pdf' -delete 2>/dev/null || true