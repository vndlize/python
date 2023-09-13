import cv2 as cv

# image1
image1_path = 'C:/Users/hridy/Desktop/images/rose1.jpg'
image1 = cv.imread(image1_path, cv.IMREAD_GRAYSCALE)

# image2
image2_path = 'C:/Users/hridy/Desktop/images/rose2.jpg'
image2 = cv.imread(image2_path, cv.IMREAD_GRAYSCALE)

# create SIFT objects for both images
sift = cv.SIFT_create()

# detect keypoints and compute descriptors for both images
keypoints1, descriptors1 = sift.detectAndCompute(image1, None)
keypoints2, descriptors2 = sift.detectAndCompute(image2, None)

# create a brute-force matcher
bf = cv.BFMatcher()

# match descriptors between the two images
matches = bf.knnMatch(descriptors1, descriptors2, k=2)

# Apply ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

# Draw the first 10 matches (you can adjust the number as needed)
matching_result = cv.drawMatches(image1, keypoints1, image2, keypoints2, good_matches[:10], None)

# Resize
scale_percent = 50  # adjust this value as needed
width = int(matching_result.shape[1] * scale_percent / 100)
height = int(matching_result.shape[0] * scale_percent / 100)
final_comparison = cv.resize(matching_result, (width, height))

# Display the matching result
cv.imshow('SIFT Matching Result', final_comparison)
cv.waitKey(0)
cv.destroyAllWindows()
