#!/usr/bin/python3
# Use GPIO buttons to control mpd on a Raspberry Pi.
# By Johnny Sprada 
# https://github.com/jsprada/mpdbuttons
# 
#
# GPIOs reserved for HifiBerry DAC:
# 2, 3, 18, 19, 20, 21
#
# GPIOs designated for Button Controls:
# 4, 5, 6, 13, 17, 22, 27, 12
#
# Control         GPIO      Pin
# Play/pause      4         7   brown
# Vol. Up         17        11  red
# Vol. Dn         27        13  orange
# Next track      6         31  yellow
# Prev. track     22        15  green
# Next Playlist   5         29  blue
# Prev. Playlist  13        33  purple

import RPi.GPIO as GPIO
import time
import mpd
import os
import longpress

# bounce time in ms
bounce = 300
longpress_bounce = 100
longpress_time = 2000

vol_variance = 5

play_pause = 4
vol_up = 17
vol_dn = 27
next = 6
prev = 22
dummy_channel = 12 # no physical button connected

buttons = (play_pause, vol_up, vol_dn, next, prev, dummy_channel)

lp_buttons = {}
lp_buttons[play_pause] = longpress.NewButton(play_pause)
lp_buttons[next] = longpress.NewButton(next)
lp_buttons[prev] = longpress.NewButton(prev)


def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buttons, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def client_connect():
    client = mpd.MPDClient()
    client.connect("localhost", 6600)
    return client

def rise_or_fall_callback(channel):
    if GPIO.input(channel):
        print(" * Release Callback")
        button_release_event(channel)
    else:
        print("* Press Callback")
        button_press_event(channel)

def button_press_event(channel):
    lp_buttons[channel].set_press_time()
    press_time = lp_buttons[channel].press_time
    time.sleep(.1)
    print("  press event:  %s" % press_time)

def button_release_event(channel):
    lp_buttons[channel].set_release_time()
    time.sleep(.2)
    press_length = lp_buttons[channel].elapsed_time
    release_time = lp_buttons[channel].release_time
    print("  release event: %s" % release_time )
    print("   elapsed: %s" % press_length )
    if press_length <= longpress_time:
        ''' short press event '''
        if channel == play_pause:
            play_pause_short(channel)
        elif channel == next:
            next_short(channel)
        elif channel == prev:
            prev_short(channel)
        else:
            print("Short press event not defined: ", channel)

    else:
        ''' long press event '''
        if channel == play_pause:
            play_pause_long(channel)
        elif channel == next:
            next_long(channel)
        elif channel == prev:
            prev_long(channel)
        else:
            print("long press event not defined: ", channel)



def play_pause_short(channel):
    print("Play Pause Short Press: ", channel)

    
    client = client_connect()
    
    status = client.status()

    if status['state'] == 'stop':
        client.play()
    elif status['state'] == 'play':
        client.pause()
    elif status['state'] == 'pause':
        client.play()
    else:
        print("Error?")

    status = client.status()
    client.disconnect()
    #print(status.items())
    print("State: ", status['state'])

def play_pause_long(channel):
    print("Shutdown: ", channel)
    shutdown()

def vol_up_callback(channel):
    print(channel)
    print("Vol Up")
    
    client = client_connect()
    status = client.status()
    vol = status['volume']
    target_vol = int(vol) + vol_variance
    client.setvol(target_vol)    
    print(client.status()['volume'])
    client.disconnect()

def vol_dn_callback(channel):
    print(channel)
    print("Vol Down")
    
    client = client_connect()
    status = client.status()
    vol = status['volume']
    target_vol = int(vol) - vol_variance
    client.setvol(target_vol)
    print(client.status()['volume'])
    client.disconnect()
    

def next_short(channel):
    print(channel)
    print("Next Track")
    
    client = client_connect()
    client.next()
    client.disconnect()
    

def prev_short(channel):
    print(channel)
    print("Previous Track")
    
    client = client_connect()
    client.previous()
    client.disconnect()


def next_long(channel):
    print(channel)
    print("Next Playlist")
    
    #client = client_connect()
    #print(client.playlist())
    #client.disconnect()


def prev_long(channel):
    print(channel)
    print("Previous Playlist")
    
    #client = client_connect()
    #print(client.playlist())
    #client.disconnect()


def dummy():
    GPIO.wait_for_edge(dummy_channel, GPIO.FALLING)
    print("Dummy Event Detected")
    
    
def stop():
    print("Stopping")
    client = client_connect()
    client.stop()
    client.close()
    client.disconnect()
    #GPIO.cleanup()  # best not to clean up, because this device is an appliance.     

def shutdown():
    stop()
    print("Shutdown Event")
    #os.system("systemctl poweroff")


def main():
    init()
    GPIO.add_event_detect(play_pause, GPIO.BOTH, callback=rise_or_fall_callback, bouncetime=longpress_bounce)
    GPIO.add_event_detect(next, GPIO.BOTH, callback=rise_or_fall_callback, bouncetime=longpress_bounce)
    GPIO.add_event_detect(prev, GPIO.BOTH, callback=rise_or_fall_callback, bouncetime=longpress_bounce)
    GPIO.add_event_detect(vol_up, GPIO.FALLING, callback=vol_up_callback, bouncetime=bounce)
    GPIO.add_event_detect(vol_dn, GPIO.FALLING, callback=vol_dn_callback, bouncetime=bounce)

    try:
        dummy()

    except KeyboardInterrupt:
        stop()

if __name__ == "__main__":
    main()
    stop()

