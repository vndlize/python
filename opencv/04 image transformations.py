
import cv2

# Load the image
image = cv2.imread('opencv/99 Sunflower2.jpg')

# Check if the image is loaded successfully
if image is not None:
    # Display the original image
    cv2.imshow('Original Image', image)
    
    # 1. Image Resizing
    # Resize the image to a specific width and height
    resized_image = cv2.resize(image, (300, 200))
    cv2.imshow('Resized Image', resized_image)

    # 2. Image Rotation
    # Rotate the image by 45 degrees
    rows, cols = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
    cv2.imshow('Rotated Image', rotated_image)

    # 3. Image Flipping
    # Flip the image horizontally
    flipped_image = cv2.flip(image, 1)
    cv2.imshow('Flipped Image', flipped_image)

    # 4. Image Cropping
    # Crop a region of interest (ROI) from the image
    x, y, width, height = 100, 50, 200, 150
    cropped_image = image[y:y+height, x:x+width]
    cv2.imshow('Cropped Image', cropped_image)

    # Wait for a key press and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found. Make sure to provide the correct image path.")
