# Frame Reading , Writing , Resizing
import cv2 as cv 


# RESIZING FUNCTION ( ONLY WORKS FOR LIVE VIDEOS )
def ChangeRes (width,height) :
    capture.set (3,width) 
    capture.set (4,height) 

# RESCALING FUNCTION 
def ResizeFrame ( frame , scale = 0.75 ) : # scale is ratio by which dimensions are multiplied
    width = int ( frame.shape[1] * scale )
    height = int ( frame.shape[0] * scale )
    dimensions = ( width , height )
    return cv.resize (frame , dimensions , interpolation=cv.INTER_AREA)


# IMAGE READING AND DISPLAYING
img = cv.imread ('99 Sunflower1.jpg') # read image
cv.imshow ( 'flower' , img ) # display image
cv.waitKey(0)


# VIDEO READING AND DISPLAYING 
capture = cv.VideoCapture ('99 yume nikki.mp4') # capture is an instance of VideoCapture
while True :
    isTrue, frame = capture.read() # Frame by Frame Reading
    cv.imshow ('Video',frame) # Frame by Frame Displaying 
    if cv.waitKey(20) & 0xFF==ord('d') : # if D key pressed , break loop 
        break 
capture.release() # release capture device
cv.destroyAllWindows() # destroy all windows since not needed


# DISPLAYING RESCALED VIDEO / IMAGES
resized_image = ResizeFrame (img)
cv.imshow ('Flower' , resized_image)
