#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source .venv/bin/activate

SCENE="${1:?Usage: ./render.sh <scene_name> [--gif]
  Examples:
    ./render.sh long_division_792
    ./render.sh long_division_7992 --gif}"

GIF=false
[[ "${2:-}" == "--gif" ]] && GIF=true

# Derive CamelCase class name from snake_case scene name
# e.g. long_division_792 → LongDivision792
CLASS=$(python3 -c "print(''.join(w.capitalize() for w in '${SCENE}'.split('_')))")

rm -rf "media/videos/${SCENE}/"

if $GIF; then
    manim -pqh --format gif "scenes/${SCENE}.py" "$CLASS"
    echo ""
    echo "→ media/videos/${SCENE}/1080p60/${CLASS}.gif"
else
    manim -pqh "scenes/${SCENE}.py" "$CLASS"
    echo ""
    echo "→ media/videos/${SCENE}/1080p60/${CLASS}.mp4"
fi
