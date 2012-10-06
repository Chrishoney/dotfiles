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

This will backup any existing files in the list  
of files listed below under "Included files" in  
the folder they are located in.  Files will be  
named 'filename.<ext>'

### delete all bash dotfiles in home

`./makelinks.py --wipe <os>`

## Included Files

'''

files = '\n'.join('* ' + fname for fname in os.listdir('mac'))

print header + files
