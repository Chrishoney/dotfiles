#!/usr/bin/env python

INCLUDE = (
    .bash_aliases,
    .bash_functions,
    .bash_profile,
    .bashcolors,
    .bashrc,
    .profile
)

IGNORE = (
    .git,
    .gitignore,
    .makelinks.py.swp,
    README.head,
    README.md,
    readme.sh
)

ignore = IGNORE
include = INCLUDE
