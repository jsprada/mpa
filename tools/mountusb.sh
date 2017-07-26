#!/bin/sh

MUSICDIR='/var/lib/mpd/'
USBDIR='/media/usb/music/'

if [ -d "$USBDIR" ]; then
	echo "true"
	sudo unlink $MUSICDIR/music
	sudo rm -rf $MUSICDIR/music
	sudo ln -s $USBDIR $MUSICDIR
	mpc update

elif [ ! -d "$USBDIR" ]; then
	echo "false"
fi




