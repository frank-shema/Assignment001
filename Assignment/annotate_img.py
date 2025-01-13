import cv2


# Read the image
image = cv2.imread('../Basic_Operations/assignment-001-given.jpg')

# Validate if the image is loaded
if image is None:
    raise FileNotFoundError("The image file was not found. Check the path and try again.")

# Coordinates for the region of interest (ROI)
top_left_x, top_left_y = 261, 198
bottom_right_x, bottom_right_y = 989, 924

# Draw a green rectangle around the ROI
cv2.rectangle(image, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 6)

# Coordinates for the transparent box
box_top_left_x, box_top_left_y = 809, 73
box_bottom_right_x, box_bottom_right_y = 1266, 194

# Text and styling settings
text = "RAH972U"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 3.2
thickness = 7
font_color = (0, 255, 0)  # Green

# Calculate the size of the text
(text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)

# Position the text to be centered in the transparent box
text_x = box_top_left_x + (box_bottom_right_x - box_top_left_x - text_width) // 2
text_y = box_top_left_y + (box_bottom_right_y - box_top_left_y + text_height) // 2

# Create a copy of the image to draw the transparent box
overlay = image.copy()

# Draw the transparent box
dark_color = (0, 0, 0)  # Black (dark color for transparency)
alpha = 0.4  # Transparency level
cv2.rectangle(overlay, (box_top_left_x, box_top_left_y), (box_bottom_right_x, box_bottom_right_y), dark_color, -1)

# Blend the overlay with the original image
cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

# Add the green text on top of the transparent box
cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, thickness)

# Display the final image
cv2.imshow('Image', image)

# Wait for any key press and save the result before closing
cv2.waitKey(0)
cv2.imwrite('myResults.jpg', image)
cv2.destroyAllWindows()
