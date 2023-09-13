import cv2 as cv
import numpy as np

# create two sample images (black and white)
image1 = np.zeros((200, 200), dtype=np.uint8)  # black image
image2 = 255 * np.ones((200, 200), dtype=np.uint8)  # white image

# create a binary mask
mask = np.zeros((200, 200), dtype=np.uint8)
mask[50:150, 50:150] = 255  # white rectangle in the center

# bitwise AND
result_and = cv.bitwise_and(image1, image2)

# bitwise OR
result_or = cv.bitwise_or(image1, image2)

# bitwise XOR
result_xor = cv.bitwise_xor(image1, image2)

# bitwise NOT
result_not = cv.bitwise_not(image1)

# bitwise AND with mask
result_masked = cv.bitwise_and(image1, image2, mask=mask)

# display the results
cv.imshow('image 1', image1)
cv.imshow('image 2', image2)
cv.imshow('mask', mask)
cv.imshow('bitwise AND', result_and)
cv.imshow('bitwise OR', result_or)
cv.imshow('bitwise XOR', result_xor)
cv.imshow('bitwise NOT', result_not)
cv.imshow('bitwise AND with mask', result_masked)

cv.waitKey(0)
cv.destroyAllWindows()
