import cv2
import numpy as np
cap = cv2.VideoCapture(0)
dispW = 1920
dispH = 1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

def TrackHueLow(value):
    global huelow 
    huelow = value
    print("Hue Low -- ", huelow)
    
def TrackHueHigh(value):
    global huehigh 
    huehigh = value
    print("Hue High -- ", huehigh)

def TrackSatLow(value):
    global satlow 
    satlow = value
    print("Sat Low -- ", satlow)

def TrackSatHigh(value):
    global sathigh
    sathigh = value
    print("Sat High -- ", sathigh)

def TrackValLow(value):
    global vallow 
    vallow = value
    print("Val Low -- ", vallow)

def TrackValHigh(value):
    global valhigh
    valhigh = value
    print("Val High -- ", valhigh)




cv2.namedWindow("HSV Trackbars")
imgDummy = np.zeros((1, 500, 3), np.uint8)
cv2.imshow('HSV Trackbars', imgDummy)
cv2.createTrackbar("Hue Low","HSV Trackbars",10, 179, TrackHueLow)
cv2.createTrackbar("Hue High","HSV Trackbars",30, 179, TrackHueHigh)
cv2.createTrackbar("Sat Low","HSV Trackbars",100, 255, TrackSatLow)
cv2.createTrackbar("Sat High","HSV Trackbars",255, 255, TrackSatHigh)
cv2.createTrackbar("Val Low","HSV Trackbars",100, 255, TrackValLow)
cv2.createTrackbar("Val High","HSV Trackbars",255, 255, TrackValHigh)


if not cap.isOpened():
    print("❌ Camera not opened")
    exit()

while True:
    ret, frame = cap.read()
    lowerbound = np.array([huelow, satlow, vallow])
    upperbound = np.array([huehigh,sathigh,valhigh])

    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV,lowerbound, upperbound)
    mymask = cv2.resize(mask,(int(dispH/2),int(dispW/2)))

    object_of_interest = cv2.bitwise_and(frame, frame, mask=mask)
    object_of_interest_final = cv2.resize(object_of_interest, (int(dispH/2), int(dispW/2)))

    cv2.imshow("Camera",frame)
    cv2.imshow("mymask" , mymask)
    cv2.imshow("object of interest" , object_of_interest_final)
    
    
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()


