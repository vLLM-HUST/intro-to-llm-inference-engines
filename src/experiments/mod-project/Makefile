PANDOC ?= pandoc
CHROMIUM ?= chromium
OUT_DIR := ../../../build/experiments/mod-project
SHEET_PDF := $(OUT_DIR)/vLLM-HUST_MOD_个人项目实验单.pdf

.PHONY: all list clean

all: $(SHEET_PDF)

list:
	@printf '%s\n' sheet.md

$(SHEET_PDF): sheet.md print.html
	@mkdir -p "$(OUT_DIR)"
	@set -eu; work=$$(mktemp -d); trap 'rm -rf "$$work"' EXIT; \
		$(PANDOC) sheet.md --from markdown --standalone --to html5 \
			--metadata lang=zh-CN --metadata pagetitle="vLLM-HUST MOD 个人项目实验单" \
			--include-in-header=print.html -o "$$work/sheet.html"; \
		"$(CHROMIUM)" --headless --disable-gpu --no-pdf-header-footer \
			--user-data-dir="$$work/profile" --print-to-pdf="$$work/sheet.pdf" "$$work/sheet.html"; \
		test -s "$$work/sheet.pdf"; \
		cp "$$work/sheet.pdf" "$@"

clean:
	@rm -f "$(SHEET_PDF)"
