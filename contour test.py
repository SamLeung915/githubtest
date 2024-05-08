import numpy as np
import cv2
import imutils

canvas = np.zeros((500, 500), dtype=np.uint8)
circle = cv2.circle(canvas, (250, 250) , 100, 10, -1)
cv2.imshow("Circle", circle)
cv2.waitKey(3000)

blurred = cv2.GaussianBlur(circle, (5, 5), 0)
thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY)[1] #This is probably key
cv2.imshow("thresh", thresh)
cv2.waitKey(0)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for cnt in cnts:
    circumference = cv2.arcLength(cnt, True)
    area = cv2.contourArea(cnt)
    print("c: %s" % circumference)
    print("area: %s" % area)
    final_image = cv2.drawContours(circle, [cnt], -1, (0, 255, 0), 2)
    cv2.imshow("Final image", final_image)
    cv2.waitKey(0)
