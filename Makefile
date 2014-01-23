cwd = $(abspath .)
# version = $(notdir $(cwd))
# component = $(notdir $(patsubst %/, %, $(dir $(cwd))))

sources:
	git clone https://github.com/facebook/flashcache.git ./flashcache-1.0.20140121
