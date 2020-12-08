#install requirements

import cv2   #computer vision

import numpy as np
import time

video=cv2.VideoCapture(0,cv2.CAP_DSHOW) #start your default laptop camera
                                        #1,2 if you don't have a camera on your laptop
time.sleep(3)  #time to open cam
for i in range(60): #time to store image
    check,background = video.read() #use loop to get precise image
background = np.flip(background, axis=1) #flip image

while(video.isOpened()):
    check,img=video.read()
    if check==False:
        break #checking weather its working
    img=np.flip(img,axis=1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert to hsv from rbg
                                                #detect colours better
    lower_red = np.array([0,120,50])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red = np.array([170,120,70])  #range for red
    upper_red = np.array([180,255,255]) #can be modified to any colour
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask1 = mask1+mask2 #detect all ranges of red

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))
    mask2 = cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(img,img, mask=mask2)
    res2 = cv2.bitwise_and(background,background, mask=mask1)
#to replace the background image in place of the colour red
    final = cv2.addWeighted(res1, 1, res2, 1, 0)
    cv2.imshow("final",final)
    key = cv2.waitKey(1)
    #to close the window and break the loop
    if key== ord('c'):
        break

video.release()
cv2.destroyAllWindows()

#RUN IT!
#MAKE GOOD USE OF IT ;)
