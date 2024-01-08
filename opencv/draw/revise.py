import cv2
import numpy as np

# Function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 0, 255), thickness=10)

# Create a named window and set mouse callback
cv2.namedWindow(winname='kitty')
cv2.setMouseCallback('kitty',draw_circle)

# Read the image
img = cv2.imread("/home/user/Documents/projects/image-processing-w-python/Images/pretty_cat.jpeg")

# Check if the image is loaded successfully
if img is None:
    print("Error: Could not load the image")
    exit()

# Main loop
while True:
    cv2.imshow('kitty', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
