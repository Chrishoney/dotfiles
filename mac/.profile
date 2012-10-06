# mac os x .profile - chrishoney@gmail.com

export PATH=/usr/local/bin:/usr/local/share/python:$PATH:$HOME/bin

rc="$HOME/.bashrc"

if [[ -f $rc ]]; then
    source $rc
fi
