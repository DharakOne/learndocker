FROM gitpod/workspace-postgres

#
# Setup the repository
#

# Install the public key for the repository (if not done previously):
run curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add \
    &&  sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'\
    &&  sudo apt install pgadmin4 \
    &&  sudo apt install pgadmin4-desktop \
    &&  sudo apt install pgadmin4-web \
    &&  sudo /usr/pgadmin4/bin/setup-web.sh


# Create the repository configuration file:
#
# Install pgAdmin
#
# Install for both desktop and web modes:
# Install for desktop mode only:
# Install for web mode only: 
# Configure the webserver, if you installed pgadmin4-web:

