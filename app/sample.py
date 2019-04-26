
def lastFirst(firstName, lastName):
    separator = ', '
    result = lastName + separator + firstName
    return result

print(lastFirst('Benjamin', 'Franklin'))
print(lastFirst('Andrew', 'Harrington'))




# Standard imports
import cv2
import numpy as np;

# Read image
im = cv2.imread("se3.jpg", cv2.IMREAD_GRAYSCALE)

#Apply treshold
ret,im = cv2.threshold(im,240,255,cv2.THRESH_BINARY)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(im,kernel,iterations = 3)
opening = cv2.morphologyEx(im, cv2.MORPH_OPEN, kernel)
im = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)


# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

#filter by color
params.filterByColor = True
params.blobColor = 255

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.4

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
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle        corresponds to the size of blob
#im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]),   (0,0,255),     cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
#cv2.imwrite("keypoints.jpg",im_with_keypoints)
print("Total of objects")
print(len(keypoints))






















import cv2
import numpy
import matplotlib.pyplot as pyplot

s1 = cv2.imread("sbp1.jpg")
s1 = cv2.resize(s1, (300, 300))
s2 = cv2.imread("sbp2.jpg")
s2 = cv2.resize(s2, (300, 300))
s3 = cv2.imread("sbp3.jpg")
s3 = cv2.resize(s3, (300, 300))
s1 = cv2.cvtColor(s1, cv2.COLOR_RGB2GRAY)
s2 = cv2.cvtColor(s2, cv2.COLOR_RGB2GRAY)
s3 = cv2.cvtColor(s3, cv2.COLOR_RGB2GRAY)
s1_white_count=0
s1_black_count=0
s2_white_count=0
s2_black_count=0
s3_white_count=0
s3_black_count=0
p = s1.shape
rows, cols= p
for i in range(rows):
    for j in range(cols):
        if s1[i, j] == 255:
            s1_white_count = s1_white_count + 1
        else:
            s1_black_count = s1_black_count + 1
print (p, s1_white_count, s1_black_count)

p = s2.shape
rows, cols= p
for i in range(rows):
    for j in range(cols):
        if s2[i, j] == 255:
            s2_white_count = s2_white_count + 1
        else:
            s2_black_count = s2_black_count + 1
print (p, s2_white_count, s2_black_count)

p = s3.shape
rows, cols= p
for i in range(rows):
    for j in range(cols):
        if s3[i, j] == 255:
            s3_white_count = s3_white_count + 1
        else:
            s3_black_count = s3_black_count + 1
print (p, s3_white_count,s3_black_count)

cv2.imshow('s1', s1)
cv2.imshow('s2', s2)
cv2.imshow('s3', s3)
cv2.waitKey(0)
cv2.destroyAllWindows()








import cv2


def desity(picture):
    picture = cv2.resize(picture, (300, 300))
    picture = cv2.cvtColor(picture, cv2.COLOR_RGB2GRAY)
    p = picture.shape
    picture_white_count=0
    rows, cols = p
    for i in range(rows):
        for j in range(cols):
            if picture[i, j] == 255:
                picture_white_count = picture_white_count + 1
    print("white count is ",picture_white_count)
    if(picture_white_count<14000):
        return 1
    else: return 0



s1 = cv2.imread("sbp1.jpg")
s2 = cv2.imread("sbp2.jpg")
s3 = cv2.imread("sbp3.jpg")
s1_white=desity(s1)
s2_white=desity(s2)
s3_white=desity(s3)
print("s1_white=",s1_white,"s2_white=",s2_white,"s3_white=",s3_white)
cv2.imshow('s1', s1)
cv2.imshow('s2', s2)
cv2.imshow('s3', s3)
cv2.waitKey(0)
cv2.destroyAllWindows()












