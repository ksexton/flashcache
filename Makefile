cwd = $(abspath .)
# version = $(notdir $(cwd))
# component = $(notdir $(patsubst %/, %, $(dir $(cwd))))

sources:
# curl -o flashcache-master.tar.gz https://codeload.github.com/facebook/flashcache/tar.gz/master
    git clone https://github.com/facebook/flashcache.git flashcache-$(date +%Y%m%d)git
    tar -cf flashcache-$(date +%Y%m%d)git.tar flashcache-$(date +%Y%m%d)git
    gzip flashcache-$(date +%Y%m%d)git.tar
    rm -fr flashcache-$(date +%Y%m%d)git
