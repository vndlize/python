import cv2
import numpy as np

# load the image
image = cv2.imread('opencv/99 Sunflower2.jpg')
# check if the image is loaded successfully
if image is not None:
    # display the original image
    cv2.imshow('original image', image)

    # convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayscale image', gray_image)

    # apply gaussian blur to the grayscale image
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    cv2.imshow('blurred image', blurred_image)

    # perform edge detection using the canny edge detector
    edges = cv2.Canny(blurred_image, 50, 150)
    cv2.imshow('edge detection', edges)

    # find and draw contours on the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_image = np.zeros_like(image)
    cv2.drawContours(contour_image, contours, -1, (0, 0, 255), 2)
    cv2.imshow('contours', contour_image)

    # threshold the grayscale image
    ret, thresholded_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
    cv2.imshow('thresholded image', thresholded_image)

    # invert the colors of the thresholded image
    inverted_image = cv2.bitwise_not(thresholded_image)
    cv2.imshow('inverted image', inverted_image)

    # wait for a key press and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image not found. make sure to provide the correct image path.")
