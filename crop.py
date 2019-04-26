import cv2
import numpy as np
import matplotlib.pyplot as pyplot

# reading the image
image = cv2.imread("im1.png")
imb = cv2.resize(image, (960, 340))
imb1 = cv2.resize(image, (960, 340))
imb = cv2.cvtColor(imb, cv2.COLOR_RGB2GRAY)
cv2.imshow("rey", imb)
cv2.waitKey(0)
ret, imb = cv2.threshold(imb, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("hi", imb)
cv2.waitKey(0)

kernel = np.ones((15, 15), np.uint8)
erosion = cv2.erode(imb, kernel, iterations=1)
cv2.imshow('erosion', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
# DIALATION OF IMAGE AND MORPHOLOGICAL OPENING
dilation = cv2.dilate(erosion, kernel, iterations=2)
cv2.imshow('dilation', dilation)
#cv2.waitKey(0)
cv2.destroyAllWindows()
edged = cv2.Canny(dilation, 10, 250)
cv2.imshow("Edges", edged)
#cv2.waitKey(0)
# applying closing function
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closed", closed)
cv2.waitKey(0)
cv2.destroyAllWindows()

# finding_contours
count=0
index=0
(_,cnts,_) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
s_no=np.zeros((4))
o_cnts_x=np.zeros((3))
cnts_x=np.zeros((3))
o_cnts=np.zeros((3,4))
contours = sorted(cnts, key=cv2.contourArea, reverse=True)
for c in contours :
    if count < 3:
        x, y, w, h = cv2.boundingRect(c)
        cnts_x[count]=x
    count = count + 1

o_cnts_x=sorted(cnts_x)
count=0

for c in contours :
    if count < 3:
        x, y, w, h = cv2.boundingRect(c)
        if o_cnts_x[0]==x:
            o_cnts[0]=cv2.boundingRect(c)
            s1 = imb1[y - 5:y + h + 5, x - 15:x + w + 5]
    count=count+1
count=0
for c in contours:
    if count < 3:
        x, y, w, h = cv2.boundingRect(c)
        x, y, w, h = cv2.boundingRect(c)
        if o_cnts_x[1] == x:
            o_cnts[1] = cv2.boundingRect(c)
            s2 = imb1[y - 5:y + h + 5, x - 15:x + w + 5]
    count = count + 1
count=0
for c in contours:
    if count < 3:
        x, y, w, h = cv2.boundingRect(c)
        if o_cnts_x[2] == x:
            o_cnts[2] = cv2.boundingRect(c)
            s3 = imb1[y - 5:y + h + 5, x - 15:x + w + 5]
    count = count + 1

print("ordered cnts")
print(o_cnts)

#cv2.rectangle(dilation, (x - 15, y - 5), (x + w + 5, y + h + 5), (0, 255, 0), 2)
cv2.imshow('s1', s1)
cv2.imshow('s2', s2)
cv2.imshow('s3', s3)
cv2.waitKey(0)
cv2.waitKey(0)
'''''
for c in contours:
    count=count+1
    if count<4 :
        index = 0
        for main_c in cnts :
            #print(cv2.boundingRect(c),cv2.boundingRect(main_c))
            if cv2.boundingRect(c)==cv2.boundingRect(main_c) :
                s_no[count]=index
                print(cv2.boundingRect(c), cv2.boundingRect(main_c))
            index = index + 1
print(s_no)
s_no=sorted(s_no)
index_cnts=0
for c in cnts:
    if (s_no[1]) == index_cnts :
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(dilation, (x - 15, y - 5), (x + w + 5, y + h + 5), (0, 255, 0), 2)
        s = imb1[y - 5:y + h + 5, x - 15:x + w + 5]
        filename = "s1.jpg"
        cv2.imwrite(filename, s)
        cv2.imshow("Output", s)
        cv2.waitKey(0)
        index_cnts = index_cnts + 1

index_cnts=0
for c in cnts:
    if (s_no[2]) == index_cnts :
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(dilation, (x - 15, y - 5), (x + w + 5, y + h + 5), (0, 255, 0), 2)
        s = imb1[y - 5:y + h + 5, x - 15:x + w + 5]
        filename = "s2.jpg"
        cv2.imwrite(filename, s)
        cv2.imshow("Output", s)
        cv2.waitKey(0)
    index_cnts = index_cnts + 1
'''



'''''
        cv2.rectangle(dilation, (x-15 , y-5), (x + w+5, y + h+5), (0, 255, 0), 2)
        s = imb1[y-5:y+h+5, x-15:x+w+5]
        filename = "s%d.jpg" %count
        print(filename)
        cv2.imwrite(filename,s)
        cv2.imshow("Output", s)
        cv2.waitKey(0)
'''''
#print(s_no)
#cv2.imshow("Output", dilation)
#cv2.waitKey(0)
'''''
_,contours,_ = cv2.findContours(closed,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
cnt=contours[max_index]
x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(imb1,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("Show",imb1)
cv2.imwrite("imaes/img5_rect.jpg", imb1 )

contours,hierarchy = cv2.findContours(closed,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
x,y,w,h = cv2.boundingRect(cnt)

crop = imb1[y:y+h,x:x+w]
cv2.imwrite('sofwinres.png',crop)
'''
cv2.waitKey(0)