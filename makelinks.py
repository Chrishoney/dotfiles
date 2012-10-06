#!/usr/bin/env python
"""makelinks.py

Create symlinks to the correct dotfiles.

Usage:
  makelinks.py [--wipe] [OS]
  makelinks.py [--backup <ext>] [OS]
  makelinks.py -h | --help

Arguments:
  OS  [linux, mac]

Options:
  -h --help       Show this screen.
  --wipe          Delete existing dotfiles
  --backup <ext>  Backup existing dotfiles with given extension

"""
import os
import shutil
import sys

# try importing the system library first
try:
    from docopt import docopt
except ImportError:
    from lib.docopt import docopt

LINK_PATH = os.environ['HOME']
INCLUDE = (
    ".bash_aliases",
    ".bash_functions",
    ".bash_profile",
    ".bashcolors",
    ".bashrc",
    ".profile"
)

os_choices = ('linux', 'mac')
dotfile_names = INCLUDE
link_path = LINK_PATH

def dotlinks(path=link_path):
    return [os.path.join(path, fname) for fname in dotfile_names]

def dotfiles(os_choice, path=None):
    path = os.getcwd()
    if not os_choice in os.listdir(path):
        sys.exit('folder %s is missing' % os_choice) 
    path = os.path.join(path, os_choice)
    return [os.path.join(path, fname) for fname in dotfile_names]

def make_links(files):
    for pair in files:
        try:
            os.symlink(*pair)
        except OSError:
            sys.exit('Please run with --wipe or --backup')

def wipe(files):
    for fname in files:
        try:
            os.unlink(os.path.join(link_path, fname))
        except OSError:
            pass

def backup(files, ext=None):
    if not ext:
        ext = '.old'
    for fname in files:
        src = os.path.join(link_path, fname)
        dst = src + ext
        shutil.move(src, dst)

if __name__ == '__main__':
    args = docopt(__doc__)
    if not args['OS']:
        sys.exit(__doc__)
    files, links = dotfiles(args['OS']), dotlinks()
    if args['--wipe']:
        wipe(links)
    elif args['--backup']:
        backup(links, args['--backup'])
    pairs = zip(files, links)
    make_links(pairs)
