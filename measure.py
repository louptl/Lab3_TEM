import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Global variables to store points and scaling factor
points = []
resize_factor = 0.5  # Factor to resize the image for display

# Callback function for mouse events
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Store the scaled-up points based on the resize factor
        points.append((int(x / resize_factor), int(y / resize_factor)))
        cv2.circle(image_resized, (x, y), 5, (0, 0, 255), -1)  # Mark point on the resized image

        # Draw line if we have two points
        if len(points) % 2 == 0:
            # Draw line on resized image for feedback
            cv2.line(image_resized, (int(points[-2][0] * resize_factor), int(points[-2][1] * resize_factor)),
                     (int(points[-1][0] * resize_factor), int(points[-1][1] * resize_factor)), (255, 0, 0), 2)
            cv2.imshow("Image", image_resized)

# Load the image and convert it to OpenCV format
folder_path = '/Users/louptl/Desktop/NTNU/Material physics/Lab 3/Lab3_6/PNG/'
image_path = f'{folder_path}P2_cl100cm_SAED_Tx6p5_Tym3p6.png'  # Replace with your .tif file path
image = Image.open(image_path)
image = np.array(image)

# Convert RGB to BGR for OpenCV display
if image.shape[-1] == 3:
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# Resize the image for display purposes
height, width = image.shape[:2]
image_resized = cv2.resize(image, (int(width * resize_factor), int(height * resize_factor)))

# Display the resized image and set mouse callback
cv2.imshow("Image", image_resized)
cv2.setMouseCallback("Image", click_event)
print("Click to draw the first line (scale), then draw the second line to measure the distance.")
cv2.waitKey(0)  # Wait until user closes the window
cv2.destroyAllWindows()

# Calculate scale based on first line and distance for the second line
if len(points) >= 4:
    # Scale line points (in original image dimensions)
    x1, y1 = points[0]
    x2, y2 = points[1]
    scale_distance_px = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Set a known scale for the scale line (replace with actual scale measurement)
    scale_length_units = 5  # nm

    # Calculate pixels per unit
    px_per_unit = scale_distance_px / scale_length_units
    print(f"Scale: {scale_length_units} units corresponds to {scale_distance_px:.2f} pixels.")

    # Measured line points (in original image dimensions)
    x3, y3 = points[2]
    x4, y4 = points[3]
    measured_distance_px = np.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)

    # Convert pixel distance to units
    measured_distance_units = measured_distance_px / px_per_unit
    print(f"Measured distance: {measured_distance_units:.2f} units.")

else:
    print("Insufficient points selected. Please select two points for each line.")
