import cv2
import numpy as np

# Load the image
image = cv2.imread('opencv/99 Sunflower2.jpg', 0)  # Load image in grayscale

# Check if the image is loaded successfully
if image is not None:
    # Define a kernel for morphological operations
    kernel = np.ones((5, 5), np.uint8)

    # Display the original image
    cv2.imshow('Original Image', image)

    # 1. Erosion
    erosion = cv2.erode(image, kernel, iterations=1)
    cv2.imshow('Erosion', erosion)

    # 2. Dilation
    dilation = cv2.dilate(image, kernel, iterations=1)
    cv2.imshow('Dilation', dilation)

    # 3. Opening (Erosion followed by Dilation)
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    cv2.imshow('Opening', opening)

    # 4. Closing (Dilation followed by Erosion)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('Closing', closing)

    # 5. Morphological Gradient (Dilation - Erosion)
    gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow('Morphological Gradient', gradient)

    # Wait for a key press and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found. Make sure to provide the correct image path.")
