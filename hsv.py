import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)
dispW = 1920
dispH = 1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)
satlow = 15
sathigh = 35
huelow=100
huehigh = 115
vallow = 80
valhigh = 110


lowerbound = np.array([huelow, satlow, vallow])
upperbound = np.array([huehigh,sathigh,valhigh])


if not cap.isOpened():
    print("❌ Camera not opened")
    exit()

while True:
    ret, frame = cap.read()
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # created a filter which matches the range of HSV of the object of interest
    mask = cv2.inRange(frameHSV,lowerbound,upperbound)
    masksmall = cv2.resize(mask,(int(dispH), int(dispW)))
    # bitwise and to filter out the pixels / image from the frame matching the mask / filter.
    object_of_interest = cv2.bitwise_and(frame, frame, mask=mask)
    object_of_interest_small = cv2.resize(object_of_interest, (int(dispH), int(dispW)))
    
    print(frameHSV[int(dispH/2), int(dispW/2)])
    #time.sleep(1)
    cv2.imshow("Camera",frame)
    cv2.imshow("Tracking Camera", masksmall)
    cv2.imshow("Object of Interest", object_of_interest_small)
    
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()


