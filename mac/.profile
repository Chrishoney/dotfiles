# mac os x .profile - chrishoney@gmail.com

export PATH=/usr/local/bin:/usr/local/sbin:/usr/local/share/python:$PATH:$HOME/bin

if [[ -f "$HOME/.bashrc" ]]; then
    source "$HOME/.bashrc"
fi

if [ -f $(brew --prefix)/etc/autojump ]; then
  . $(brew --prefix)/etc/autojump.sh
fi
