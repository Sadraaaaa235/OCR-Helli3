import cv2
import numpy as np

image = cv2.imread(r'C:\Users\SONY\Desktop\Programming\Helli3-Project\example\zVLoH.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 150)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

largest_contour = max(contours, key=cv2.contourArea)
rect = cv2.minAreaRect(largest_contour)
angle = rect[-1]
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated_image = cv2.warpAffine(image, M, (w, h))
cv2.imshow('test', rotated_image)
cv2.waitKey()