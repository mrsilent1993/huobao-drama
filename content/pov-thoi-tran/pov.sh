#!/usr/bin/env bash
# Ghép các clip POV, thêm tiêu đề mở đầu, mốc giờ cho từng cảnh và dòng chữ kết.
#
# Cách dùng:
#   ./pov.sh plan.txt out.mp4
#   CLIP_SECONDS=5 ./pov.sh plan.txt out-30s.mp4   # chỉ lấy 5 giây đầu mỗi clip (bản ngắn)
#
# plan.txt (dòng trống và dòng bắt đầu bằng # được bỏ qua; " / " là xuống dòng):
#   title: POV: Bạn là dân thường / thời Trần
#   end: Năm 1285, quân dân Đại Việt / đánh tan quân Nguyên Mông.
#   clip: tran-1.mp4 | Giờ Dần · 4 giờ sáng
#   clip: tran-2.mp4 | Giờ Mão · 6 giờ sáng
#
# Cần ffmpeg có bộ lọc drawtext (ffmpeg của hệ thống).
set -euo pipefail
[ $# -eq 2 ] || { sed -n '2,13p' "$0"; exit 1; }

PLAN=$1; OUT=$2
BASE=$(cd "$(dirname "$PLAN")" && pwd)
FONT=${POV_FONT:-/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf}
W=720; H=1280
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

title=""; end=""; files=(); caps=()
while IFS= read -r line || [ -n "$line" ]; do
  line=${line%$'\r'}
  case "$line" in
    ''|'#'*) ;;
    title:*) title=$(echo "${line#title:}" | sed 's/^ *//') ;;
    end:*)   end=$(echo "${line#end:}" | sed 's/^ *//') ;;
    clip:*)  rest=${line#clip:}
             f=$(echo "${rest%%|*}" | sed 's/^ *//; s/ *$//')
             [ "${f:0:1}" = / ] || f="$BASE/$f"
             files+=("$f"); caps+=("$(echo "${rest#*|}" | sed 's/^ *//')") ;;
    *) echo "Dòng không hiểu: $line" >&2; exit 1 ;;
  esac
done <"$PLAN"
[ ${#files[@]} -gt 0 ] || { echo "plan.txt chưa có clip nào" >&2; exit 1; }

# Ghi chữ ra file để không phải thoát ký tự trong filtergraph; " / " thành xuống dòng.
put() { printf '%s' "$2" | sed 's# / #\n#g' >"$TMP/$1.txt"; }
text() {  # text <file> <fontsize> <y> [enable]
  local e=${4:+:enable=\'$4\'}
  printf "drawtext=fontfile=%s:textfile=%s:fontsize=%s:fontcolor=white:line_spacing=10:borderw=3:bordercolor=black@0.85:x=(w-tw)/2:y=%s%s" \
    "$FONT" "$TMP/$1.txt" "$2" "$3" "$e"
}

inputs=(); chain=""; n=${#files[@]}
for ((i = 0; i < n; i++)); do
  f=${files[$i]}
  [ -f "$f" ] || { echo "Không thấy file: $f" >&2; exit 1; }
  inputs+=(-i "$f")
  dur=$(ffprobe -v error -select_streams v:0 -show_entries stream=duration -of csv=p=0 "$f")
  [ -n "${CLIP_SECONDS:-}" ] && dur=$(echo "if ($dur < $CLIP_SECONDS) $dur else $CLIP_SECONDS" | bc)
  put "cap$i" "${caps[$i]}"
  v="[$i:v]trim=0:$dur,setpts=PTS-STARTPTS,scale=$W:$H:force_original_aspect_ratio=increase,crop=$W:$H,setsar=1,fps=24"
  v+=",$(text "cap$i" 40 170 "lt(t,3.5)")"
  if [ $i -eq 0 ] && [ -n "$title" ]; then put title "$title"; v+=",$(text title 44 "h*0.42" "lt(t,3)")"; fi
  if [ $i -eq $((n - 1)) ] && [ -n "$end" ]; then
    put end "$end"
    v+=",drawbox=x=0:y=ih*0.38:w=iw:h=ih*0.2:color=black@0.55:t=fill:enable='gte(t,$dur-3)'"
    v+=",$(text end 36 "h*0.42" "gte(t,$dur-3)")"
  fi
  chain+="$v,format=yuv420p[v$i];"
  chain+="[$i:a]aresample=48000,aformat=channel_layouts=stereo,loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000,"
  chain+="atrim=0:$dur,asetpts=PTS-STARTPTS,afade=t=in:d=0.05,afade=t=out:st=$(echo "$dur - 0.05" | bc):d=0.05[a$i];"
done
for ((i = 0; i < n; i++)); do chain+="[v$i][a$i]"; done
chain+="concat=n=$n:v=1:a=1[v][a]"

ffmpeg -v error -y "${inputs[@]}" -filter_complex "$chain" -map "[v]" -map "[a]" \
  -c:v libx264 -preset medium -crf 20 -c:a aac -b:a 192k -movflags +faststart "$OUT"
echo "Đã xuất: $OUT"
