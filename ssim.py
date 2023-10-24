import cv2
import numpy as np
from skimage import color, measure
import os
import subprocess
import re
from skimage import io, color
from skimage.metrics import structural_similarity as ssim


def extract_frames(video_file):
    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return []

    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frames.append(frame)

    cap.release()

    return frames



def calc_ssim_between_keyframes(keyframes1, keyframes2):
    ssim_scores = []

    for keyframe1 in keyframes1:
        for keyframe2 in keyframes2:
            keyframe1_gray = color.rgb2gray(keyframe1)
            keyframe2_gray = color.rgb2gray(keyframe2)

            ssim_score = ssim(keyframe1_gray, keyframe2_gray,data_range=1.0)
            ssim_scores.append(ssim_score)

            print("SSIM Score:", ssim_score)

        break


    return ssim_scores

if __name__ == "__main__":
    video_file1 = 'output.ts'  # Replace with your input file paths
    video_file2 = 'output_crop.ts'

    keyframes1 = extract_frames(video_file1)
    keyframes2 = extract_frames(video_file2)

    print(f"Number of Keyframes in Video 1: {len(keyframes1)}")
    print(f"Number of Keyframes in Video 2: {len(keyframes2)}")

    calc_ssim_between_keyframes(keyframes2, keyframes1)

