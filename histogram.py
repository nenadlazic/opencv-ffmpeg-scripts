import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image1 = cv2.imread('first_frame.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('second_frame.jpg', cv2.IMREAD_GRAYSCALE)


# Calculate the histogram
histogram1 = cv2.calcHist([image1], [0], None, [256], [0, 256])
histogram2 = cv2.calcHist([image2], [0], None, [256], [0, 256])

# Calculate the Bhattacharyya distance
bhattacharyya_distance = cv2.compareHist(histogram1, histogram2, cv2.HISTCMP_BHATTACHARYYA)

# Convert Bhattacharyya distance to similarity within 0-100 range
similarity_percentage = max(0, (1 - bhattacharyya_distance) * 100)

print(f"Similarity Percentage: {similarity_percentage:.2f}")

# Plot both histograms
plt.figure(figsize=(8, 4))
plt.title('Histogram Comparison')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Plot histogram1 in blue and histogram2 in red
plt.plot(histogram1, color='blue', label='Image 1')
plt.plot(histogram2, color='red', label='Image 2')

plt.legend()
plt.xlim([0, 256])
plt.show()


