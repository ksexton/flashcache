cwd = $(abspath .)
version = $(shell date +%Y%m%d)git

sources:
	git clone https://github.com/facebook/flashcache.git ./flashcache-$(version)
	tar -cf flashcache-$(version).tar flashcache-$(version)
	gzip flashcache-$(version).tar
	rm -fr flashcache-$(version)
