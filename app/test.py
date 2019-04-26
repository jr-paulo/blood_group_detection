# Standard imports
import cv2
import numpy as np;


im = cv2.imread("san1.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow('segment', im)
#Apply treshold
ret,im = cv2.threshold(im,240,255,cv2.THRESH_BINARY)

kernel = np.ones((5,6),np.uint8)

#erosion = cv2.erode(im,kernel,iterations = 3)
im = cv2.erode(im,kernel,iterations = 2)
#cv2.imshow('segment2', erosion)
#opening = cv2.morphologyEx(im, cv2.MORPH_OPEN, kernel)
#cv2.imshow('segment3', opening)
#im = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
cv2.imshow('segment4', im)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

#filter by color
params.filterByColor = True
params.blobColor = 255

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.01

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else :
    detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
#cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle        corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]),   (0,0,255),     cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
cv2.imwrite("keypoints.jpg",im_with_keypoints)
print("Total of objects")
print(len(keypoints))

cv2.waitKey(0)
cv2.destroyAllWindows()