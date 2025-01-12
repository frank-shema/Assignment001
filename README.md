# Annotating an Image Using OpenCV

This README provides a comprehensive guide on how to annotate an image by adding a rectangle and text with a transparent background using OpenCV. The coordinates are derived using an Image Map Generator and the reference image provided by the instructor.

## Table of Contents
- [Dependencies](#dependencies)
- [Overview](#overview)
- [Step-by-Step Implementation](#step-by-step-implementation)
  - [1. Setting Up the Environment](#1-setting-up-the-environment)
  - [2. Reading the Image](#2-reading-the-image)
  - [3. Drawing the Rectangle](#3-drawing-the-rectangle)
  - [4. Adding Text with a Transparent Background](#4-adding-text-with-a-transparent-background)
  - [5. Displaying and Saving the Annotated Image](#5-displaying-and-saving-the-annotated-image)
- [Code Walkthrough](#code-walkthrough)
- [Result](#result)

---

## Dependencies

Ensure the following dependencies are installed:

- Python 3.x
- OpenCV library (`cv2`)

To install OpenCV, run the following command:

```bash
pip install opencv-python
```

---

## Overview

The annotation process involves:

1. **Highlighting a Region of Interest (ROI):** Drawing a green rectangle around the ROI.
2. **Adding a Transparent Background:** Drawing a semi-transparent box to enhance text visibility.
3. **Overlaying Text:** Centering text within the transparent box.

This process can be used in various image processing tasks, including object detection and labeling.

---

## Step-by-Step Implementation

### 1. Setting Up the Environment

- Import the OpenCV library.
- Prepare the image and ensure it is correctly loaded using `cv2.imread()`.
- Validate the image path to avoid runtime errors.

### 2. Reading the Image

Load the image using the following code:

```python
image = cv2.imread('../Basic_Operations/assignment-001-given.jpg')

if image is None:
    raise FileNotFoundError("The image file was not found. Check the path and try again.")
```

### 3. Drawing the Rectangle

Define the coordinates of the ROI and draw a green rectangle around it:

```python
top_left_x, top_left_y = 261, 198
bottom_right_x, bottom_right_y = 989, 924

cv2.rectangle(image, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 6)
```

### 4. Adding Text with a Transparent Background

- **Transparent Box:**
  - Create an overlay of the original image.
  - Draw a dark rectangle with a transparency factor (`alpha`).

```python
box_top_left_x, box_top_left_y = 809, 73
box_bottom_right_x, box_bottom_right_y = 1266, 194

overlay = image.copy()
dark_color = (0, 0, 0)
alpha = 0.4
cv2.rectangle(overlay, (box_top_left_x, box_top_left_y), (box_bottom_right_x, box_bottom_right_y), dark_color, -1)
cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)
```

- **Adding Text:**
  - Calculate the text size and position it within the transparent box.

```python
text = "RAH972U"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 3.2
thickness = 7
font_color = (0, 255, 0)

(text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)
text_x = box_top_left_x + (box_bottom_right_x - box_top_left_x - text_width) // 2
text_y = box_top_left_y + (box_bottom_right_y - box_top_left_y + text_height) // 2
cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, thickness)
```

### 5. Displaying and Saving the Annotated Image

- Display the annotated image in a new window:

```python
cv2.imshow('Image', image)
cv2.waitKey(0)
```

- Save the annotated image to a file:

```python
cv2.imwrite('myResults.jpg', image)
cv2.destroyAllWindows()
```

---

## Code Walkthrough

Below is the full code with comments:

```python
import cv2

# Read the image
image = cv2.imread('../Basic_Operations/assignment-001-given.jpg')
if image is None:
    raise FileNotFoundError("The image file was not found. Check the path and try again.")

# Coordinates for the region of interest (ROI)
top_left_x, top_left_y = 261, 198
bottom_right_x, bottom_right_y = 989, 924
cv2.rectangle(image, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 6)

# Coordinates for the transparent box
box_top_left_x, box_top_left_y = 809, 73
box_bottom_right_x, box_bottom_right_y = 1266, 194

# Create overlay for transparency
overlay = image.copy()
dark_color = (0, 0, 0)
alpha = 0.4
cv2.rectangle(overlay, (box_top_left_x, box_top_left_y), (box_bottom_right_x, box_bottom_right_y), dark_color, -1)
cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

# Add text to the transparent box
text = "RAH972U"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 3.2
thickness = 7
font_color = (0, 255, 0)

(text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)
text_x = box_top_left_x + (box_bottom_right_x - box_top_left_x - text_width) // 2
text_y = box_top_left_y + (box_bottom_right_y - box_top_left_y + text_height) // 2
cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, thickness)

# Display and save the result
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.imwrite('myResults.jpg', image)
cv2.destroyAllWindows()
```

---

## Result

After running the script, you will get:

1. A green rectangle highlighting the ROI.
2. A dark transparent box with centered green text overlay.
3. The output image saved as `myResults.jpg` in the current working directory.

---

SHEMA FRANK



