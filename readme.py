#!/usr/bin/env python
import os

header = '''## Installation

* `./makelinks.py <os>`
* `./makelinks.py --backup <ext> <os>`

### Wipe

`./makelinks.py <os>`

WARNING!!
This removes all files being replaced without confirmation and creates
symlinks in their place.
WARNING!!

### Backup

`./makelinks.py --backup <ext> <os>`

This will backup any existing files that would be deleted by a wipe.
Files will be named 'filename.<ext>' inside ~/. After the files are
backed up, they are deleted and the symlinks are created.

Note: If the existing dotfiles are symlinks, no backups will be made,
and the old symlinks will be silently removed.

## Included Files

'''

files = '\n'.join('* ' + fname for fname in os.listdir('mac'))

print header + files
