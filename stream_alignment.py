import cv2
import numpy as np
import os
import sys

def get_histograms_from_video(video_file):
    cap = cv2.VideoCapture(video_file)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return []

    histograms = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        curr_histogram = cv2.calcHist([gray_frame], [0], None, [256], [0, 256])

        video_file_name = os.path.splitext(os.path.basename(video_file))[0]

        output_file = f"{video_file_name}_frame.jpg"

        cv2.imwrite(output_file, frame)

        histograms.append(curr_histogram)

    cap.release()

    return histograms


def calculate_similarity(histogram1, histogram2):
    bhattacharyya_distance = cv2.compareHist(histogram1, histogram2, cv2.HISTCMP_BHATTACHARYYA)

    similarity_percentage = max(0, (1 - bhattacharyya_distance) * 100)

    #print("SIMILARITY:", similarity_percentage)

    return similarity_percentage



def find_max_similarity_index(histograms_ref, histograms_dst, pattern_size):
    if pattern_size > len(histograms_ref) or pattern_size > len(histograms_dst):
        raise ValueError("Pattern size is larger than the histogram arrays")

    max_similarity = -1
    max_similarity_index = -1

    for i in range(len(histograms_ref) - pattern_size + 1):
        total_similarity = 0
        for j in range(pattern_size):
            total_similarity += calculate_similarity(histograms_ref[i + j], histograms_dst[j])

        if total_similarity > max_similarity:
            max_similarity = total_similarity
            max_similarity_index = i
            print("SET MAX: total:", total_similarity)
            print("SET MAX: ref frame index:", i)
            print("SET MAX: dst frame index:", j-pattern_size+1)

    return max_similarity_index


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python steam.py file1 file2")
        sys.exit(1)

    video_file_ref = sys.argv[1]
    video_file_dst = sys.argv[2]

    histograms_ref = get_histograms_from_video(video_file_ref)
    print("Size of histograms_ref:", len(histograms_ref))


    histograms_dst = get_histograms_from_video(video_file_dst)
    print("Size of histograms_dst:", len(histograms_dst))


    pattern_size = 100
    max_similarity_index = find_max_similarity_index(histograms_ref, histograms_dst, pattern_size)

    print("Index with maximum total similarity:", max_similarity_index)