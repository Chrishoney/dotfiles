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

This will backup any existing files listed below under "Included files"
in the folder they are located in. Files will be named 'filename.<ext>'
The original files are deleted after the backups are created.

Note: If the existing dotfiles are symlinks, no backups will be made,
and the old symlinks will be silently removed.

## Included Files

'''

files = '\n'.join('* ' + fname for fname in os.listdir('mac'))

print header + files
