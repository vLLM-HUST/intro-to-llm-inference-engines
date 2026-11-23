.PHONY: all experiments list clean

all: experiments

experiments:
	@$(MAKE) -C src/experiments/mod-project

list:
	@$(MAKE) -C src/experiments/mod-project list

clean:
	@$(MAKE) -C src/experiments/mod-project clean
