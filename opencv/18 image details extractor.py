import cv2

image_path = 'opencv/Sunflower2.jpg'  
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not open or read the image.")
else:
    height, width, channels = image.shape
    print(f"Image dimensions: {width}x{height}")
    print(f"Number of color channels: {channels}")

    for y in range(3):  # Limit to the first 3 rows for brevity
        row_info = ""
        for x in range(3):  # Limit to the first 3 columns for brevity
            pixel_value = image[y, x]
            row_info += f"{pixel_value} "
        print(row_info)

    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
