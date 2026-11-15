#!/usr/bin/env bash
# Ghép các clip và phủ hiệu ứng camera giám sát (CCTV / camera chuông cửa).
#
# Cách dùng:
#   ./cctv.sh "<dòng ngày giờ>" "<tên camera>" <giờ bắt đầu HH:MM:SS> <file ra.mp4> clip1.mp4 [clip2.mp4 ...]
# Ví dụ:
#   ./cctv.sh "Hùng Vương thứ 18 · giờ Mão" "CAM CỔNG CHÍNH" 06:12:40 tap1.mp4 tap1-a.mp4 tap1-b.mp4
#
# Cần ffmpeg có bộ lọc drawtext (ffmpeg của hệ thống; bản ffmpeg-static trong backend không có).
set -euo pipefail

if [ $# -lt 5 ]; then
  sed -n '2,8p' "$0"; exit 1
fi

LABEL=$1; CAM=$2; START=$3; OUT=$4; shift 4
FONT=${CCTV_FONT:-/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf}
[ -f "$FONT" ] || FONT=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf
W=720; H=1280

# Giờ bắt đầu -> số giây, để đồng hồ trên hình chạy liên tục qua các clip.
IFS=: read -r hh mm ss <<<"$START"
EPOCH=$((10#$hh * 3600 + 10#$mm * 60 + 10#$ss))

# Viết chữ vào file tạm để không phải thoát ký tự đặc biệt trong filtergraph.
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
printf '%s' "$LABEL" >"$TMP/label.txt"
printf '%s' "$CAM" >"$TMP/cam.txt"

inputs=(); chain=""; n=0
for f in "$@"; do
  inputs+=(-i "$f")
  # loudnorm kéo dài đuôi âm thanh một chút; cắt về đúng độ dài hình để không lệch tiếng.
  dur=$(ffprobe -v error -select_streams v:0 -show_entries stream=duration -of csv=p=0 "$f")
  chain+="[$n:v]scale=$W:$H:force_original_aspect_ratio=increase,crop=$W:$H,setsar=1,fps=24,format=yuv420p[v$n];"
  chain+="[$n:a]aresample=48000,aformat=channel_layouts=stereo,loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000,"
  chain+="atrim=0:$dur,asetpts=PTS-STARTPTS,afade=t=in:d=0.05,afade=t=out:st=$(echo "$dur - 0.05" | bc):d=0.05[a$n];"
  n=$((n + 1))
done
for ((i = 0; i < n; i++)); do chain+="[v$i][a$i]"; done
chain+="concat=n=$n:v=1:a=1[cv][ca];"

chain+="[cv]lenscorrection=k1=-0.12:k2=-0.02,crop=iw*0.94:ih*0.94,scale=$W:$H,"
chain+="eq=saturation=0.6:contrast=1.08:brightness=-0.02,colorbalance=bs=0.03:gs=0.02,"
chain+="noise=alls=9:allf=t,vignette=PI/4.5,"
chain+="drawbox=x=0:y=0:w=iw:h=96:color=black@0.45:t=fill,"
chain+="drawtext=fontfile=$FONT:textfile=$TMP/label.txt:x=22:y=16:fontsize=26:fontcolor=white,"
chain+="drawtext=fontfile=$FONT:text='%{pts\\:gmtime\\:$EPOCH\\:%H\\\\\\:%M\\\\\\:%S}':x=22:y=54:fontsize=28:fontcolor=white,"
chain+="drawtext=fontfile=$FONT:textfile=$TMP/cam.txt:x=w-tw-22:y=54:fontsize=24:fontcolor=white,"
chain+="drawtext=fontfile=$FONT:text='● REC':x=22:y=h-58:fontsize=26:fontcolor=red:enable='lt(mod(t\\,1)\\,0.6)',"
chain+="format=yuv420p[v];[ca]anull[a]"

ffmpeg -v error -y "${inputs[@]}" -filter_complex "$chain" -map "[v]" -map "[a]" \
  -c:v libx264 -preset medium -crf 20 -c:a aac -b:a 192k -movflags +faststart "$OUT"
echo "Đã xuất: $OUT"
