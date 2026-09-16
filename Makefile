.PHONY: all clean preview help init archive

DATE := $(shell date +%Y%m%d)
OUTPUT_DIR := output
OUTPUT_FILE := $(OUTPUT_DIR)/newsletter_$(DATE).html

all: $(OUTPUT_FILE)

$(OUTPUT_FILE): contents/content.md template.html newsletter.py
	@mkdir -p $(OUTPUT_DIR)
	python3 newsletter.py contents/content.md template.html $(OUTPUT_FILE)

preview: $(OUTPUT_FILE)
	@echo "Opening newsletter..."
	@if grep -qi microsoft /proc/version 2> /dev/null; then \
		explorer.exe "$$(wslpath -w $(OUTPUT_FILE))" || true; \
	elif command -v xdg-open > /dev/null; then \
		xdg-open $(OUTPUT_FILE); \
	elif command -v open > /dev/null; then \
		open $(OUTPUT_FILE); \
	else \
		echo "Please open $(OUTPUT_FILE) manually"; \
	fi

clean:
	rm -rf $(OUTPUT_DIR)/

init:
	pip install -r requirements.txt

# 아카이브 디렉토리로 복사
archive: $(OUTPUT_FILE)
	@mkdir -p archive
	cp $(OUTPUT_FILE) archive/
	@echo "Archived to archive/newsletter_$(DATE).html"

help:
	@echo "Newsletter Builder - Makefile Commands"
	@echo "======================================"
	@echo "  make          - Generate newsletter"
	@echo "  make preview  - Generate and preview"
	@echo "  make archive  - Copy to archive folder"
	@echo "  make clean    - Remove generated files"
	@echo "  make init     - Install Python dependencies"