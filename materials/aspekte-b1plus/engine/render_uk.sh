#!/bin/bash
# Рендер беззвучного відео + звук з оригіналу без перекодування
V=$1; A=/mnt/project-files/tiktok-german/aspekte-b1plus/$V; cd /home/user/uk/$V
(cd proj && npx hyperframes render -o ../silent.mp4 > ../render.log 2>&1) || { echo "FAIL $V"; exit 1; }
ffmpeg -y -v error -i silent.mp4 -i $A/$V.mp4 -map 0:v -map 1:a -c copy -shortest -movflags +faststart ${V}_uk.mp4
echo "done $V $(ffprobe -v error -show_entries format=duration -of csv=p=0 ${V}_uk.mp4)"
