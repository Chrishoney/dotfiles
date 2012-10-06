# Instructions

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

* .bash_aliases
* .bash_functions
* .bash_profile
* .bashcolors
* .bashrc
* .profile
