#!/bin/bash
# Копирует готовый ролик в папку проекта и в папку страницы-артефакта
N=$1; D=/mnt/project-files/tiktok-german/aspekte-b1plus/$N; S=/tmp/claude-0/-home-user-frases-words/cd2ae7f0-51c3-5953-b936-79b6645f69e0/scratchpad/site
mkdir -p $D/project && cd /home/user/gv/$N && cp $N.mp4 subtitles_de.srt $D/ && cp timeline.json proj/index.html $D/project/ && cp ../$N.py $D/project/spec.py && cp $N.mp4 $S/
ffprobe -v error -show_entries format=duration -of csv=p=0 $N.mp4
