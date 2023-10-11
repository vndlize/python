import cv2 as cv

# image1
image1_path = 'opencv/99 Sunflower1.jpg'
image1 = cv.imread(image1_path, cv.IMREAD_GRAYSCALE)

# image2
image2_path = 'opencv/99 Sunflower2.jpg'
image2 = cv.imread(image2_path, cv.IMREAD_GRAYSCALE)

# create ORB objects for both images
orb = cv.ORB_create()

# detect keypoints and compute descriptors for both images
keypoints1, descriptors1 = orb.detectAndCompute(image1, None)
keypoints2, descriptors2 = orb.detectAndCompute(image2, None)

# create a brute-force matcher
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

# match descriptors between the two images
matches = bf.match(descriptors1, descriptors2)

# sort the matches by their distance (lower distance means better match)
matches = sorted(matches, key=lambda x: x.distance)

# draw the first 10 matches (you can adjust the number as needed)
matching_result = cv.drawMatches(image1, keypoints1, image2, keypoints2, matches[:10], None)

# resize
scale_percent = 50  # adjust this value as needed
width = int(matching_result.shape[1] * scale_percent / 100)
height = int(matching_result.shape[0] * scale_percent / 100)
final_comparison = cv.resize(matching_result, (width, height))

# display the matching result
cv.imshow('orb matching result', final_comparison)
cv.waitKey(0)
cv.destroyAllWindows()
