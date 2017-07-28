#MPA Build Doc

1) Dowload Raspbian Lite Image

2) Burn to SD Card
  
3) Connect keyboard, Screen, Ethernet

4) Log in:
   login: pi
   passowrd: raspberry

5) Follow Instructions at MPA repository:
   https://github.com/jsprada/mpa

   $ sudo apt-get update
   $ sudo apt-get install git
      #? force yes to apt-getn b
   $ git clone https://github.com/jsprada/mpa
   $ cd mpa
   $ sudo sh install.sh

## install.sh

system config:
	update
	change hostname
	change locale
	remove pi user
	create mpd user
	setup wifi
	enable ssh

Install pre-reqs:

y