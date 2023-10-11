# OPEN CV TRANSFORMATIONS 
import cv2 as cv
img = cv.imread ('opencv/99 Sunflower1.jpg')
cv.imshow ( 'flower' , img )

# greyscale 
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow ( 'greyscale' , grey )

# blur
blur = cv.GaussianBlur (img , (7,7), cv.BORDER_DEFAULT) # the (7,7) is the kernel size and can be + - accordingly
cv.imshow ('blur' , blur)

# edge cascade 
cannyedge = cv.Canny (img , 125 , 175)
cv.imshow ('canny edges' , cannyedge)

# dilation
dilated = cv.dilate (cannyedge , (3,3) , iterations=1)
cv.imshow ('dilated' , dilated)

# eroding
eroded = cv.erode (dilated , (3,3) , iterations= 1)
cv.imshow ('eroded' , eroded)

# eroding and dilation are considered as morphological transformations

# resizing 
resized = cv.resize ( img , (500,500)) # the (500,500) are dimensions here
cv.imshow ('resized' , resized)

cv.waitKey(0)

