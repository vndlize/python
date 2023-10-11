import cv2 as cv

# Load two images for comparison
image1_path = 'opencv/99 Sunflower1.jpg'
image2_path = 'opencv/99 Sunflower2.jpg'

image1 = cv.imread(image1_path, cv.IMREAD_GRAYSCALE)
image2 = cv.imread(image2_path, cv.IMREAD_GRAYSCALE)

# Create an AKAZE object
akaze = cv.AKAZE_create()

# Detect keypoints and compute descriptors for both images
keypoints1, descriptors1 = akaze.detectAndCompute(image1, None)
keypoints2, descriptors2 = akaze.detectAndCompute(image2, None)

# Create a Brute-Force Matcher
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

# Match descriptors between the two images
matches = bf.match(descriptors1, descriptors2)

# Sort the matches by their distance (lower distance means better match)
matches = sorted(matches, key=lambda x: x.distance)

# Draw the first 10 matches (you can adjust the number as needed)
matching_result = cv.drawMatches(image1, keypoints1, image2, keypoints2, matches[:10], None)

# Resize function
def resize_image(image, scale_percent=50):  
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    resized_image = cv.resize(image, (width, height))
    return resized_image

resized_matching_result = resize_image (matching_result)

# Display the matching result
cv.imshow('AKAZE Matching Result', resized_matching_result)
cv.waitKey(0)
cv.destroyAllWindows()
