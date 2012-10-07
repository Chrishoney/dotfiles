# mac osx x .bashrc - chrishoney@gmail.com

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

# force ignoredups and ignorespace
export HISTCONTROL=ignoreboth
# remove history size limit, append to history
export HISTFILESIZE=
export HISTSIZE=
shopt -s histappend

# update the values of LINES and COLUMNS as necessary
shopt -s checkwinsize

# make less more friendly for non-text input files, see lesspipe(1)
#[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "$debian_chroot" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color) color_prompt=yes;;
esac

# colored prompt
force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ] && [ -f ~/.bashcolors ]; then
    source ~/.bashcolors
    PS1="\[$cyan\]\u\[$lightgrey\]@\[$cyan\]\h\[$lightgrey\]:\[$blue\]\w\[$lightgrey\]\$\[\033[0m\] "
else
    PS1='\u@\h:\w\$ '
fi

unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;\u@\h: \w\a\]$PS1"
    ;;  
*)
    ;;
esac

# enable color support of ls
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
fi

# enable bash completion for tons of programs.
# this requires the 'bash-completion' package
#
# for a full list of supported programs:
# `find $(brew --prefix)/etc/bash_completion.d/ | sed 's|^.*\/\/||`
if [ -f $(brew --prefix)/etc/bash_completion ]; then
    source $(brew --prefix)/etc/bash_completion
fi

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

if [ -f ~/.bash_functions ]; then
    . ~/.bash_functions
fi

# set line editor to vi
set -o vi
export VISUAL=vim
export EDITOR=vim
export PYTHONDONTWRITEBYTECODE=1
