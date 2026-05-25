.PHONY: all slides tutorials experiments list clean clean-slides clean-tutorials clean-experiments

all: slides tutorials experiments

slides:
	@$(MAKE) -C src/slides

tutorials:
	@$(MAKE) -C src/tutorials

experiments:
	@$(MAKE) -C src/experiments/nano-vLLM实验课

list:
	@$(MAKE) -C src/slides list
	@$(MAKE) -C src/tutorials list
	@$(MAKE) -C src/experiments/nano-vLLM实验课 list

clean: clean-slides clean-tutorials clean-experiments

clean-slides:
	@$(MAKE) -C src/slides clean

clean-tutorials:
	@$(MAKE) -C src/tutorials clean

clean-experiments:
	@$(MAKE) -C src/experiments/nano-vLLM实验课 clean
