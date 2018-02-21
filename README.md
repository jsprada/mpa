# mpa
Music Player Appliance - Turn your Raspberry Pi into a music playing appliance

Sample song, included in `~/music` "A Deal Soon Regretted" provided by Amplitude Problem:
 

https://amplitudeproblem.bandcamp.com

## What is it?
MPA is a foundation for you to build your own music player on a Raspberry Pi.  It should be installed on a Debian based operating system, it's tested and recommended to start with Raspbian Lite.  The entire system is based on the time tested MPD (Music Player Daemon) platform, and several different clients are included for convenience.  You may chose to use some, none, or all of the clients to control playback.  The bare bones of this project will install the following packages:

* `mpd` (https://github.com/MusicPlayerDaemon/MPD), which is the heart of the system.  MPD is a server that will play your music files.  

* `ncmpcpp` (https://github.com/arybczak/ncmpcpp), which is a full featured terminal/text based client used to control the playback of music hosted by the MPD package. 

* `mpc` (https://github.com/MusicPlayerDaemon/mpc), which is a minimal client that can be used to control playback of MPD hosted songs using one-liners from the terminal.

The client and server software listed above can be used to get your music player started.  At any time, you can log in to the device using a keyboard/monitor, or SSH into it, and control playback from the command line. 

There are also two additional playback clients included in MPA:

* MPAButtonsd - Python scripts running as a daemon that will interpret button presses (buttons connected to the GPIO pins on the Pi) to control playback.   As of now, this will play/pause/skip forward or back, and poweroff the device.  These buttons will allow you to control playback like a stand-alone music playing device, or a radio that sits on the counter or a desk.  

* A Python/Flask based minimal web interface that will show the current song playing, and allow you to play/pause playback.  This can be accessed from another computer on the same network, if you browse to the mpa device on port 80.

It should be noted that this is not a complete, feature rich system.  It's the core of a system that you can add on to.   Out of the box, it will configure the Pi to play music out of the built in 3.5mm headphone jack.  You can add a DAC, amp and speakers to create a hifi device to fill a room with music if you wish. 

I'm currently working on a touch screen interface (for use in a car system, but I suppose would work anywhere!) which I'll add when it's ready. 



## Install from fresh copy of Raspbian:
    sudo apt-get update
    sudo apt-get install git
    git clone https://github.com/jsprada/mpa
    cd mpa
    sudo sh install.sh
