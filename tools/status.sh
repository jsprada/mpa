#!/bin/sh

MPD=$(systemctl is-failed mpd.service)
BUTTONS=$(systemctl is-failed mpaweb.service)
WEB=$(systemctl is-failed mpabuttonsd.service)

MPD_ENABLED=$(systemctl is-enabled mpd.service)
BUTTONS_ENABLED=$(systemctl is-enabled mpaweb.service)
WEB_ENABLED=$(systemctl is-enabled mpabuttonsd.service)

echo "---mpa status---"
echo "mpd: $MPD, $MPD_ENABLED"
echo "buttons: $BUTTONS, $BUTTONS_ENABLED"
echo "web: $WEB, $WEB_ENABLED"

