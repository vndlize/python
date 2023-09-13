import cv2 as cv
import numpy as np

img1 = cv.imread('C:/Users/HridyeshDas/OneDrive - Tata Insights and Quants/Desktop/Pictures/flower.jpg')
img2 = cv.imread('C:/Users/HridyeshDas/OneDrive - Tata Insights and Quants/Desktop/Pictures/flower2.jfif')

# for arithmetic operations always ensure images are of same dimensions
image2 = cv.resize(img2, (500, 500))
image1 = cv.resize(img1, (500, 500))

result_add = cv.add(image1, image2)
result_subtract = cv.subtract(image1, image2)
result_multiply = cv.multiply(image1, image2)
result_divide = cv.divide(image1, image2, dtype=cv.CV_32F) # avoid division by 0 

cv.imshow('image addition', result_add)
cv.imshow('image subtraction', result_subtract)
cv.imshow('image multiplication', result_multiply)
cv.imshow('image division', result_divide)
cv.waitKey(0)
cv.destroyAllWindows()
