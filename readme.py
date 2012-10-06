#!/usr/bin/env python
import os
import sys

header = '''# Instructions

## Installation

All 3 options create symlinks.

### create fresh symlinks

`./makelinks.py <os>`

### backup current files

`./makelinks.py --backup <ext> <os>`

### delete all bash dotfiles in home

`./makelinks.py --wipe <os>`

## Included Files

'''

files = '\n'.join('* ' + fname for fname in os.listdir('mac'))

print header + files
