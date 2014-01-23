cwd = $(abspath .)
# version = $(notdir $(cwd))
# component = $(notdir $(patsubst %/, %, $(dir $(cwd))))

sources:
	curl -o flashcache-1.0.20140121git.tar.gz https://github.com/facebook/flashcache/archive/master.zip
