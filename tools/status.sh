#!/bin/sh

MPD=$(systemctl is-active mpd.service)
BUTTONS=$(systemctl is-active mpaweb.service)
WEB=$(systemctl is-active mpabuttonsd.service)

MPD_ENABLED=$(systemctl is-enabled mpd.service)
BUTTONS_ENABLED=$(systemctl is-enabled mpaweb.service)
WEB_ENABLED=$(systemctl is-enabled mpabuttonsd.service)

echo "---mpa status---"
echo "mpd: $MPD, $MPD_ENABLED"
echo "buttons: $BUTTONS, $BUTTONS_ENABLED"
echo "web: $WEB, $WEB_ENABLED"

