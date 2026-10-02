import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    filtered_image = image.copy()
    if filter_type == 'red_tint':
        # Increase red channel
        filtered_image[:, :, 1] = 0  # Set green channel to 0
        filtered_image[:, :, 0] = 0  # Set blue channel to 0
    elif filter_type == 'green_tint':  
        # Increase green channel
        filtered_image[:, :, 1] = 0  # Set red channel to 0
        filtered_image[:, :, 2] = 0  # Set blue channel to 0
    elif filter_type == 'blue_tint':
        # Increase blue channel
        filtered_image[:, :, 0] = 0  # Set red channel to 0
        filtered_image[:, :, 2] = 0  # Set green channel to 0
    elif filter_type == 'increase_red':
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == 'decrease_blue':
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)
    return filtered_image

image_path = "example.jpeg" 
image = cv2.imread(image_path)
if image is None:
    print("Error: Image not found!")
else:
    filter_type = "original" # Default filter type
    print("Press the following keys to apply filters:")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - Increase Red Intensity")
    print("d - Decrease Blue Intensity")
    print("q - Quit")
    while True:
# Apply the selected filter
        filtered_image = apply_color_filter(image, filter_type)
# Display the filtered image
        cv2.imshow("Filtered Image", filtered_image)
# Wait for key press
        key = cv2.waitKey(0) & 0xFF
        # Map key presses to filters
        if key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('g'):
            filter_type = "green_tint"
        elif key == ord('i'):
            filter_type = "increase_red"
        elif key == ord('d'):
            filter_type = "decrease_blue"
        elif key == ord('q'):
            print("Exiting...")
            break
        else:
            print("Invalid key! Please use 'r', 'b', 'g', 'i', 'd', or 'q'.")
cv2.destroyAllWindows()
