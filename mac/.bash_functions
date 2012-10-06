# functions
bell () { echo -e '\x07'; }
mkcd () { mkdir $1 && cd $1; }
venv () { source ~/.venv/$1/bin/activate; }
simple () { python -m SimpleHTTPServer $1; }
web () { open http://$1; }

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
