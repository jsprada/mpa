#!/bin/sh
# Install and setup MPA on a fresh installed Debian based Raspberry Pi

sbin_dir=/usr/sbin/mpa

check_root()
{
if [ "$(id -u)" -ne 0 ] ; then
    echo "This script must be executed with root privileges."
    exit 1
fi
}


setup_system()
{
apt-get update
#apt-get install -y iw wpasupplicant wireless-tools wireless-regdb crda --no-install-recommends
apt-get install -y  $(cat packages) --no-install-recommends

sudo pip3 install python-mpd2
sudo pip3 install flask

#hostnamectl set-hostname mpa0M

#sudo rm /etc/hosts
#sudo cp ./etc/hosts /etc/hosts

#sudo rm /etc/motd
#sudo cp ./etc/hosts/motd /etc/motd

# Copy song to music dir
sudo cp ~/mpa/music/* /var/lib/mpd/music/

# set audio to play throuh 3.5mm headphone jack
# amixer cset numid=3 1

#git clone https://github.com/jsprada/mpdbuttons
#cd mpdbuttons
#sudo sh install.sh

sudo systemctl enable ssh.socket
mpc update
}

# install mpa buttonsd
install_buttons()
{

sudo mkdir -p $sbin_dir/buttons
sudo cp ./buttons/*.py $sbin_dir/buttons/

cat << _EOF_ > /etc/systemd/system/mpabuttonsd.service
[Unit]
Description=mpa buttons
BindsTo=mpd.service

[Service]
ExecStart=/usr/sbin/mpa/buttons/mpabuttonsd.py

[Install]
WantedBy=multi-user.target
_EOF_
}

install_web()
{
sudo mkdir -p $sbin_dir/web

sudo cp -r ./web/*  $sbin_dir/web

cat << _EOF_ > /etc/systemd/system/mpaweb.service
[Unit]
Description=mpa web interface
BindsTo=mpd.service

[Service]
ExecStart=/usr/bin/python3 /usr/sbin/mpa/web/app.py

[Install]
WantedBy=multi-user.target
_EOF_

}

start_new_d()
{

 systemctl enable $1
 systemctl daemon-reload
 systemctl start $1
 systemctl status $1

}

check_root
install_buttons
start_new_d mpabuttonsd.service
install_web
start_new_d mpaweb.service
#systemctl reboot
