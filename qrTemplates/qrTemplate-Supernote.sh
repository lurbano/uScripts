#!/bin/bash

# generate qr code for "https://soriki.com/uSciCalc/" in file sciCalc-qr.png
qrencode -s 6 -o sciCalc-qr.png "https://soriki.com/uSciCalc/"

# place image in NorthEast corner of canvas for supernote Nomad
composite -gravity NorthEast -geometry +50+100 sciCalc-qr.png -size 1404x1872 canvas:none sciCalc-template.png