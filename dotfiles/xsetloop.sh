#!/bin/bash
status() {
    # Volume %
    echo "V:"$(amixer sget Master | grep -o "[0-9]*%\|\[on\]\|\[off\]")

    # Battery %
    echo "B:"$(acpi -b | grep -o '[0-9]*%')

    # Current keyboard layout

    layoutValue=$(xset -q | grep LED | awk '{ print $10 }')

    case $layoutValue in
	00000000|00000001) layout="en" ;;
#	00000001) layout="EN" ;;
	00001000|00001001) layout="fr" ;;
#	00001001) layout="FR" ;;
	*) layout = "??" ;;
    esac

    echo $layout

    # Date & time
    date '+%Y %a %d %b %I:%M%p'
    
}

while :; do
    xsetroot -name "$(status | tr '\n' ' ')"
    sleep 1m
done
