import pytesseract

# Testing other methods
filename = "sample.jpg"

# Get bounding box estimates
print(pytesseract.image_to_boxes(filename))

# Get verbose data including boxes, confidences, line and page numbers
print(pytesseract.image_to_data(filename))

# Get information about orientation and script detection
print(pytesseract.image_to_osd(filename))
