#!/bin/bash

git remote add github https://github.com/nachtmaar/androlyzedoc.git
git add -A *.rst screenshots/
sh make_doc.sh
git add -A _build/html
git commit
git push github origin master
