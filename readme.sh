#!/bin/bash

dotfiles=$(find . -name '.*' | grep -Ev '(swp|git|^\.$)' | sed 's/^\./* ~/')
