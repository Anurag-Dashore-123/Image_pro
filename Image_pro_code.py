import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply blur to the image
blur = cv2.GaussianBlur(img, (5, 5), 0)

# Detect edges in the image
edges = cv2.Canny(img, 100, 200)

# Display the images
cv2.imshow('Original', img)
cv2.imshow('Grayscale', gray)
cv2.imshow('Blur', blur)
cv2.imshow('Edges', edges)

# Wait for a key press
cv2.waitKey(0)
cv2.destroyAllWindows()
