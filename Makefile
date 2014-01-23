cwd = $(abspath .)
# version = $(notdir $(cwd))
# component = $(notdir $(patsubst %/, %, $(dir $(cwd))))

sources:
	curl -o flashcache-master.tar.gz https://codeload.github.com/facebook/flashcache/tar.gz/master
