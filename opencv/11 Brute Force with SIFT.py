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

# Detect keypoints and compute descriptors for the first image
keypoints1, descriptors1 = sift.detectAndCompute(image, None)

# Draw keypoints on the first image
image_with_keypoints1 = cv.drawKeypoints(image, keypoints1, None)
resized_image_with_keypoints1 = resize_image(image_with_keypoints1, scale_percent=75)

# Display the first image with SIFT keypoints
cv.imshow('SIFT Keypoints (Image 1)', resized_image_with_keypoints1)

# Load another image for matching (you can load a different image)
image2_path = 'C:/Users/hridy/Desktop/images/rose2.jpg'
image2 = cv.imread(image2_path)
keypoints2, descriptors2 = sift.detectAndCompute(image2, None)

# Create a Brute-Force Matcher
bf = cv.BFMatcher(cv.NORM_L2, crossCheck=True)

# Match descriptors using the Brute-Force Matcher
matches = bf.match(descriptors1, descriptors2)

# Sort the matches by their distance (lower distance means better match)
matches = sorted(matches, key=lambda x: x.distance)

# Draw the first 10 matches (you can adjust the number as needed)
matching_result = cv.drawMatches(image, keypoints1, image2, keypoints2, matches[:10], None)

# Resize the matching result
resized_matching_result = resize_image(matching_result, scale_percent=50)

# Display the matching result
cv.imshow('SIFT Matching Result with Brute-Force Matcher', resized_matching_result)

cv.waitKey(0)
cv.destroyAllWindows()
