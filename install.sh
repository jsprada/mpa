#!/bin/sh
# Install and setup MPA on a fresh installed Debian based Raspberry Pi

apt-get update

#apt-get install -y iw wpasupplicant wireless-tools wireless-regdb crda --no-install-recommends

apt-get install -y  $(cat packages) --no-install-recommends

sudo pip3 install python-mpd2
sudo pip3 install flask

hostnamectl set-hostname mpa

rm /etc/hosts
mv ./etc/hosts /etc/hosts

rm /etc/motd
mv ./etc/hosts/motd /etc/motd

# Copy song to music dir
sudo cp ~/mpa/music/* /var/lib/mpd/music/

# set audio to play throuh 3.5mm headphone jack
# amixer cset numid=3 1

#git clone https://github.com/jsprada/mpdbuttons
#cd mpdbuttons
#sudo sh install.sh

sudo systemctl enable ssh.socket
=======
mpc update

systemctl reboot
