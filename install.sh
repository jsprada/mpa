apt-get install -y iw wpasupplicant wireless-tools wireless-regdb crda --no-install-recommends

apt-get install -y  mpd git python3 python3-pip rpi.gpio mpc ncmpcpp --no-install-recommends

sudo pip3 install python-mpd2


hostnamectl set-hostname mpa

cat << _EOF_ > /etc/hosts
127.0.0.1       localhost
127.0.0.1       mpa
__EOF__

cat << _EOF_ > /etc/motd

  _ __  _ __  __ _ 
 | '  \| '_ \/ _\` |
 |_|_|_| .__/\__,_|
       |_|         
 
 Music Player Appliance

 https://github.com/jsprada/mpa

_EOF_

#sudo ln -s /var/lib/mpd/music ./music
#sudo mount ./music /var/lib/mpd/music/

#systemctl reboot

