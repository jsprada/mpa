#!/bin/sh
# Install and setup MPA on a fresh installed Debian based Raspberry Pi

sbin_dir=/usr/sbin/mpa

check_root()
{
echo " checking for root"	
if [ "$(id -u)" -ne 0 ] ; then
    echo "  must be run as root!"
    exit 1
fi
}


setup_env()
{

hostnamectl set-hostname mpa

#rm /etc/hosts
#cp ./etc/hosts /etc/hosts

cat << _EOF_ > /etc/hosts
127.0.0.1       localhost
127.0.0.1       mpa
__EOF__


rm /etc/motd
#cp ./etc/hosts/motd /etc/motd
cat << _EOF_ > /etc/motd

  _ __  _ __  __ _ 
 | '  \| '_ \/ _\` |
 |_|_|_| .__/\__,_|
       |_|         
 
 Music Player Appliance

 https://github.com/jsprada/mpa

_EOF_

#git clone https://github.com/jsprada/mpdbuttons
#cd mpdbuttons
#sudo sh install.sh
#### set country code
#### connect to wifi
#### setup hostapd
}

setup_system()
{
echo" running system setup"
apt-get update
#apt-get install -y iw wpasupplicant wireless-tools wireless-regdb crda --no-install-recommends
apt-get install -y  $(cat packages) --no-install-recommends

pip3 install python-mpd2
pip3 install flask

# Copy song to music dir
cp music/* /var/lib/mpd/music/

# set audio to play throuh 3.5mm headphone jack
amixer cset numid=3 1

systemctl enable ssh.socket
mpc update
}


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

echo "MPA Insallation"
check_root
#setup_env
setup_system
install_buttons
start_new_d mpabuttonsd.service
install_web
start_new_d mpaweb.service
systemctl reboot
