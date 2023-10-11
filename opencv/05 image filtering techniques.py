import cv2 as cv
import numpy as np

# load an image
image = cv.imread ('opencv/99 Sunflower1.jpg')

# gaussian filtering
gaussian_blur = cv.GaussianBlur(image, (5, 5), 0)

# median filtering
median_blur = cv.medianBlur(image, 5)

# bilateral filtering
bilateral_blur = cv.bilateralFilter(image, 9, 75, 75)

# box (average) filtering
box_blur = cv.blur(image, (5, 5))

# erosion and dilation (example of erosion)
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(image, kernel, iterations=1)

# sobel filtering (example for x-direction)
sobel_x = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=5)

# canny edge detection
edges = cv.Canny(image, 100, 200)

# laplacian filtering
laplacian = cv.Laplacian(image, cv.CV_64F)

# scharr filtering (example for x-direction)
scharr_x = cv.Scharr(image, cv.CV_64F, 1, 0)

# prewitt filtering (example for x-direction)
kernel_prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
prewitt_x = cv.filter2D(image, -1, kernel_prewitt_x)

# custom kernel filtering (example)
custom_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
custom_filtered = cv.filter2D(image, -1, custom_kernel)

cv.imshow('original image', image)
cv.imshow('gaussian blur', gaussian_blur)
cv.imshow('median blur', median_blur)
cv.imshow('bilateral filter', bilateral_blur)
cv.imshow('box blur', box_blur)
cv.imshow('erosion', erosion)
cv.imshow('sobel x', sobel_x)
cv.imshow('canny edges', edges)
cv.imshow('laplacian', laplacian)
cv.imshow('scharr x', scharr_x)
cv.imshow('prewitt x', prewitt_x)
cv.imshow('custom kernel filtering', custom_filtered)

cv.waitKey(0)
cv.destroyAllWindows()
