#!/bin/sh

MPD=$(systemctl is-failed mpd.service)
BUTTONS=$(systemctl is-failed mpabuttonsd.service)
WEB=$(systemctl is-failed mpaweb.service)

MPD_ENABLED=$(systemctl is-enabled mpd.service)
BUTTONS_ENABLED=$(systemctl is-enabled mpabuttonsd.service)
WEB_ENABLED=$(systemctl is-enabled mpaweb.service)

echo "---mpa status---"
echo "mpd: $MPD, $MPD_ENABLED"
echo "buttons: $BUTTONS, $BUTTONS_ENABLED"
echo "web: $WEB, $WEB_ENABLED"

