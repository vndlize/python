# FLANN WITH SIFT

import cv2 as cv

# Load an image
image_path = 'C:/Users/hridy/Desktop/images/rose1.jpg'
image = cv.imread(image_path)

# Resize function
def resize_image(image, scale_percent=50):  
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    resized_image = cv.resize(image, (width, height))
    return resized_image

# Create a SIFT object
sift = cv.SIFT_create()

# Detect keypoints and compute descriptors
keypoints, descriptors = sift.detectAndCompute(image, None)

# Draw keypoints on the image
image_with_keypoints = cv.drawKeypoints(image, keypoints, None)
resized_image_with_keypoints = resize_image(image_with_keypoints, scale_percent=75)

# Display the image with SIFT keypoints
cv.imshow('SIFT Keypoints', resized_image_with_keypoints)

# Load another image for matching (you can load a different image)
image2_path = 'C:/Users/hridy/Desktop/images/rose2.jpg'
image2 = cv.imread(image2_path)
keypoints2, descriptors2 = sift.detectAndCompute(image2, None)

# Create FLANN-based matcher
flann_index_params = dict(algorithm=0, trees=5)
flann_search_params = dict(checks=50)
flann = cv.FlannBasedMatcher(flann_index_params, flann_search_params)

# Match descriptors using FLANN
matches = flann.knnMatch(descriptors, descriptors2, k=2)

# Apply ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)

# Draw matches on the images
matching_result = cv.drawMatches(image, keypoints, image2, keypoints2, good_matches, None)

# Resize the matching result
resized_matching_result = resize_image(matching_result, scale_percent=50)

# Display the matching result
cv.imshow('SIFT Matching Result with FLANN', resized_matching_result)

cv.waitKey(0)
cv.destroyAllWindows()
