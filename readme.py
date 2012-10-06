#!/usr/bin/env python
import os
import sys

header = '''# Installation

* `./makelinks.py --backup <ext>` or `./makelinks --wipe`
* `./makelinks.py <os>`

### Deal with existing files

Both of these options remove the old files after finishing.

`./makelinks.py --wipe`

--wipe removes all files being replaced without confirmation.

`./makelinks.py --backup <ext> <os>`

This will backup any existing files listed below under
"Included files" in  the folder they are located in.
Files will be named 'filename.<ext>' The original files
are deleted after the backups are created.

Note: If the existing dotfiles are symlinks, no
backups will be made, and the old symlinks will
be silently removed.

### Create fresh symlinks

`./makelinks.py <os>`

## Included Files

'''

files = '\n'.join('* ' + fname for fname in os.listdir('mac'))

print header + files
