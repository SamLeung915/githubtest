import cv2 
import imutils
#import argparse

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True, help="path to the input image")
#args = vars(ap.parse_args())


# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
image = cv2.imread("test_frame_2_13.03.jpg")
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

# convert the resized image to grayscale, blur it slightly,
# and threshold it
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
                                #This is a threshold value i.e, any pixel that has colour value above this value will be made into the specified pixel colour (value to the right)
thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)[1] #This is probably key
cv2.imshow("Thresh", thresh)

# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

#print("cnts length: ", len(cnts))
#print("cnts 7 : ", cnts[7])

for c in cnts:
	# compute the center of the contour, then detect the name of the
	# shape using only the contour
	M = cv2.moments(c)
	cX = int((M["m10"] / M["m00"]) * ratio)
	cY = int((M["m01"] / M["m00"]) * ratio)
	# multiply the contour (x, y)-coordinates by the resize ratio,
    # then draw the contours and the name of the shape on the image
	c = c.astype("float")
	c *= ratio
	c = c.astype("int")
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

	# show the output image
	cv2.imshow("Image", image)
	cv2.waitKey(0)