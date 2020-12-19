FROM gitpod/workspace-postgres

run curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add

run sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'\
    &&  sudo apt install pgadmin4 \
    &&  sudo apt install pgadmin4-desktop \
    &&  sudo apt install pgadmin4-web \
    &&  sudo /usr/pgadmin4/bin/setup-web.sh
