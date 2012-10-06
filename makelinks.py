#!/usr/bin/env python
"""makelinks.py

Create symlinks to the correct dotfiles.

Usage:
  makelinks.py OS
  makelinks.py --wipe
  makelinks.py --backup <ext>
  makelinks.py -h | --help

Arguments:
  OS  [linux, mac]

Options:
  -h --help       Show this screen.
  --wipe          Delete existing dotfiles
  --backup <ext>  Backup dotfiles as 'name'+'ext'

"""
import os
import shutil
import sys
# try importing the system library first, then lib/docopt if it fails
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
    ''' Return a list of link destination paths '''
    return [os.path.join(path, fname) for fname in dotfile_names]

def dotfiles(os_choice, path=None):
    ''' Return a list of dotfiles for the selected os '''
    path = os.getcwd()
    if not os_choice in os.listdir(path):
        sys.exit('folder %s is missing' % os_choice)
    path = os.path.join(path, os_choice)
    return [os.path.join(path, fname) for fname in dotfile_names]

def make_links(files):
    ''' Create the symlinks, fail and exit if we can't write '''
    for pair in files:
        try:
            os.symlink(*pair)
        except OSError:
            sys.exit('Please run with --wipe or --backup')

def verify_links(files):
    for link in files:
        if not os.path.islink(link):
            return False
    return True

def wipe(files):
    ''' Delete existing dotfiles, fail and exit if we can't write '''
    for fname in files:
        try:
            os.unlink(os.path.join(link_path, fname))
        except OSError:
            pass

def backup(files, ext):
    ''' Create a copy of fname at /path/to/fname.ext for each file '''
    for fname in files:
        src = os.path.join(link_path, fname)
        if os.path.islink(src) or not os.path.exists(src):
            pass
        else:
            dst = src + ext
            shutil.move(src, dst)

if __name__ == '__main__':
    args = docopt(__doc__)
    links = dotlinks()
    wipe_flag = None
    # wipe or backup and exit
    if args['--backup']:
        backup(links, args['--backup'])
        wipe_flag = True
    if args['--wipe'] or wipe_flag:
        wipe(links)
        sys.exit("Ready to link")
    # create the links
    files, = dotfiles(args['OS']),
    pairs = zip(files, links)
    make_links(pairs)
    if verify_links(links):
        sys.exit("Linking finished.")
    # This clause should never execute
    else:
        sys.exit("Unknown Error")
