alias ..='cd ..'
alias tempmail='python -m smtpd -n -c DebuggingServer localhost:1025'
alias status='~/dev/jobstoar/bin/status'
alias gitmod="git status -s | cut -d' ' -f3 | grep -v '^$'"
alias footv='telnet termcast.develz.org'
alias iftop='sudo /usr/local/sbin/iftop -i en1'

alias l='ls -A'     # list all except . and ..
alias la='ls -al'   # long listing of all
alias ll='ls -l'

#turn into a function
alias simple='python -m SimpleHTTPServer 8080'
