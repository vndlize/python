import cv2 as cv

# image loading
image_path = 'opencv/99 Sunflower1.jpg'
img = cv.imread(image_path)
image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

# resize
scale_percent = 50  # adjust this value as needed
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
smaller_image = cv.resize(image, (width, height))
smaller_img = cv.resize(img, (width, height))

# create an ORB object
orb = cv.ORB_create()

# detect keypoints and compute descriptors for the resized image
keypoints, descriptors = orb.detectAndCompute(smaller_image, None)

# draw keypoints on the resized image
image_with_keypoints = cv.drawKeypoints(smaller_image, keypoints, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# display the resized image with keypoints
cv.imshow('orb keypoints (smaller image)', image_with_keypoints)
cv.imshow('original image', smaller_img)
cv.waitKey(0)
cv.destroyAllWindows()

# optionally, you can save the smaller image with keypoints
# cv.imwrite('smaller_image_with_keypoints.jpg', image_with_keypoints)
