#!/bin/bash

# Check if both input file and frame_id arguments are provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <input_file> <frame_id>"
  exit 1
fi

# Assign the input file and frame_id arguments to variables
input_file="$1"
frame_id="$2"

# Output file name
output_file="output_frame_${frame_id}.jpg"

# FFmpeg command with the input_file and frame_id variables
ffmpeg -i "$input_file" -vf  "select=gte(n\,$frame_id)" -vframes 1 "$output_file"

echo "Frame $frame_id from $input_file saved as $output_file"

