#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage ./gop_size.sh input_file_name.mp4"
    exit 1
fi

video_file="$1"

pict_type_lines=$(ffprobe -show_frames "$video_file" | grep "pict_type")


gop_size=0 

echo "$pict_type_lines" | while IFS= read -r line; do
    echo "$line"

    if [[ "$line" == "pict_type=I" ]]; then
        echo "###### GOP SIZE: $gop_size"
	gop_size=1
    else
	((gop_size++))
    fi
done
