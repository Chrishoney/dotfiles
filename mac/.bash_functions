# functions
bell () { echo -e '\x07'; }
mkcd () { mkdir $1 && cd $1; }
venv () { source ~/.venv/$1/bin/activate; }
simple () { python -m SimpleHTTPServer $1; }
web () { open http://$1; }
mdhtml () {
    markdown --html4tags $1 | w3m -T text/html;
}

calc () {
    echo "$1" | bc
}

show_hidden () {
    if [[ $1 == "TRUE" || $1 == "FALSE" ]]; then
        defaults write com.apple.finder AppleShowAllFiles $1
        killall Finder
    else
        echo "Usage: $0 (TRUE|FALSE)"
    fi
}

crawl () {
    if [[ $1 == "cszo" ]]; then
        user="crawl"
        server="crawl.s-z.org"
    elif [[ $1 == "cao" ]]; then
        user="joshua"
        server="crawl.akrasiac.org"
    elif [[ $1 == "cdo" ]]; then
        user="crawl"
        server="crawl.develz.org"
    fi
    
    if [[ -n $user && -n $server && $# == 1 ]]; then
        ssh -C -i ~/.ssh/$1_key "$user"@"$server";
    else
        echo "Usage: crawl <server>  |  server=cao, cdo, or cszo"
    fi
}

termcast () {
    script -t 0 >( cat ~/.ratry_login - | nc noway.ratry.ru 31337 > /dev/null ) "$@"
}

s () {
    # s <arg> = source ~/.<arg>
    case "$1" in 
    vim)
        source ~/.vimrc
        ;;
    rc)
        source ~/.bashrc
        ;;
    func)
        source ~/.bash_functions
        ;;
    alias)
        source ~/.bash_aliases
        ;;
    profile)
        source ~/.bash_profile
        ;;
    esac
}
