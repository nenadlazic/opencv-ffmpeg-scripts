import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

def compare_images(image_file1, image_file2):
    # Load the images
    image1 = cv2.imread(image_file1, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image_file2, cv2.IMREAD_GRAYSCALE)

    # Calculate the histograms
    histogram1 = cv2.calcHist([image1], [0], None, [256], [0, 256])
    histogram2 = cv2.calcHist([image2], [0], None, [256], [0, 256])

    # Calculate the Bhattacharyya distance
    bhattacharyya_distance = cv2.compareHist(histogram1, histogram2, cv2.HISTCMP_BHATTACHARYYA)

    # Convert Bhattacharyya distance to similarity within 0-100 range
    similarity_percentage = max(0, (1 - bhattacharyya_distance) * 100)

    return similarity_percentage, histogram1, histogram2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_images.py image_file1 image_file2")
        sys.exit(1)

    image_file1 = sys.argv[1]
    image_file2 = sys.argv[2]

    similarity, histogram1, histogram2 = compare_images(image_file1, image_file2)

    print(f"Similarity Percentage: {similarity:.2f}")

    # Plot both histograms
    plt.figure(figsize=(8, 4))
    plt.title('Histogram Comparison')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    # Plot histogram1 in blue and histogram2 in red
    plt.plot(histogram1, color='blue', label='Image 1')
    plt.plot(histogram2, color='red', label='Image 2')

    plt.legend()
    plt.xlim([0, 256])  # Set the x-axis limits to match the pixel intensity range
    plt.show()

