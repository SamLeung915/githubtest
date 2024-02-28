import numpy as np
import cv2 as cv
import imutils

image = cv.imread('frame_2.jpg', cv.IMREAD_GRAYSCALE)
assert image is not None, "file could not be read, check with os.path.exists()"
resized = imutils.resize(image, width = 300)
ratio = image.shape[0] / float(resized.shape[0])

#ret,thresh = cv.threshold(image,127,255,0)
ret, thresh = cv.threshold(image,127,255,0)

#contours,hierarchy = cv.findContours(thresh, 1, 2)
cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#cnt = contours[0]
cnts = imutils.grab_contours(cnts)
c = cnts[0]
print("c: ", c)
#M = cv.moments(cnt)
#print( M )
M = cv.moments(c)
c = c.astype("float")
c *= ratio
c = c.astype("int")
cv.drawContours(image, [c], -1, (0, 255, 0), 2)
cv.imshow("Image", image)
cv.waitKey(0)

#cx = int(M['m10']/M['m00'])
#cy = int(M['m01']/M['m00'])

#area = cv.contourArea(cnt)

#perimeter = cv.arcLength(cnt,True)

#epsilon = 0.1*cv.arcLength(cnt,True)
#approx = cv.approxPolyDP(cnt,epsilon,True)
#print("contour: ", contours)
#cv.imshow("Image", img)
#cv.waitKey(0)
