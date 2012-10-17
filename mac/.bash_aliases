alias ..='cd ..'
alias tempmail='python -m smtpd -n -c DebuggingServer localhost:1025'
alias gitmod="git status -s | cut -d' ' -f3 | grep -v '^$'"
alias footv='telnet termcast.develz.org'
alias iftop='sudo iftop -i en1'
alias htop='sudo htop'

alias l='ls -A'     # list all except . and ..
alias la='ls -Al'   # long listing of all
alias ll='ls -l'

#turn into a function
alias venvs="find ~/.venv/ -maxdepth 1 -type d | grep -oE '\w+$'"
alias markdown='markdown --html4tags'
