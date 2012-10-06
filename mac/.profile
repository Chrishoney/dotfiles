# mac os x .profile - chrishoney@gmail.com

export PATH=/usr/local/bin:/usr/local/share/python:$PATH:$HOME/bin

if [[ -f "$HOME/.bashrc" ]]; then
    source "$HOME/.bashrc"
fi
