import cv2 as cv

# load an image
image_path = 'C:/Users/hridy/Desktop/images/rose1.jpg'
image = cv.imread(image_path)

# resize function 
def resize_image(image, scale_percent=75): # change scale percent according to use
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    resized_image = cv.resize(image, (width, height))
    return resized_image

# create a sift object
sift = cv.SIFT_create()

# detect keypoints and compute descriptors
keypoints, descriptors = sift.detectAndCompute(image, None)

# draw keypoints on the image
image_with_keypoints = cv.drawKeypoints(image, keypoints, None)
resized_image_with_keypoints = resize_image ( image_with_keypoints , scale_percent= 75)

# display the image with keypoints
cv.imshow('sift keypoints', resized_image_with_keypoints)

cv.waitKey(0)
cv.destroyAllWindows()
