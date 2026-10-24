#!/bin/bash
# Рендер серии: bash render.sh EP_ID [v|h|vh]  -> ../EP_ID/EP_ID.mp4 (вертикаль) и EP_ID_youtube.mp4 (16:9)
# запускать через: nohup setsid bash render.sh EP_ID vh > /home/user/artikel/render_EP_ID.log 2>&1 &
set -e
EP=$1; MODES=${2:-vh}; E=$(cd "$(dirname "$0")" && pwd); D=$E/../$EP
for M in $(echo $MODES | grep -o .); do
  python3 $E/gen.py $EP $M
  P=/home/user/artikel/${EP}_$M
  (cd $P && hyperframes render -o silent.mp4 --quiet)
  OUT=$D/$EP.mp4; [ $M = h ] && OUT=$D/${EP}_youtube.mp4
  ffmpeg -v error -y -i $P/silent.mp4 -i $D/song.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest $OUT
  echo "done $OUT"
done
