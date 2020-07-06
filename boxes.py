import cv2
import pytesseract

# more about boxes

img = cv2.imread("sample.jpg")

d = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
n_boxes = len(d["level"])
for i in range(n_boxes):
    (x, y, w, h) = (d["left"][i], d["top"][i], d["width"][i], d["height"][i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 1)


cv2.imwrite("output_boxes.jpg", img)
# cv2.imshow('img', img)
# cv2.waitKey(0)
