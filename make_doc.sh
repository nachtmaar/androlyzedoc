#!/bin/bash

#pandoc -f rst -t markdown index.rst -o ../README.md
#pandoc -f markdown -t rst ../README.md -o index.rst
#pandoc -f rst -t markdown index.rst -o README.md
make clean
sphinx-apidoc -f ../ -o .
make html
