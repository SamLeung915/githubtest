import numpy as np
import cv2

canvas = np.zeros((500, 500), dtype=np.uint8)
circle = cv2.circle(canvas, (250, 250) , 100, 10, -1)

contours, hierarchy = cv2.findContours(circle, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    circumference = cv2.arcLength(cnt, True)
    area = cv2.contourArea(cnt)
    print("c: %s" % circumference)
    print("area: %s" % area)