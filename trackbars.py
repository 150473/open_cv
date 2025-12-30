import cv2
import numpy as np
cap = cv2.VideoCapture(0)
dispW = 1920
dispH = 1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

def TrackX(value):
    global xpos 
    xpos = value
    print("X Pos -- ", xpos)
    
def TrackY(value):
    global ypos 
    ypos = value
    print("Y Pos -- ", ypos)

def BoxWidth(value):
    global boxwidth 
    boxwidth = value
    print("Box Width -- ", boxwidth)

def BoxHeight(value):
    global boxheight
    boxheight = value
    print("Box Height -- ", boxheight)


cv2.namedWindow("My Trackbars")
cv2.createTrackbar("X-Pos","My Trackbars",10,dispW - 1,TrackX)
cv2.createTrackbar("Y-Pos","My Trackbars",10,dispH - 1, TrackY)
cv2.createTrackbar("Box Width","My Trackbars",10,dispW - 1,BoxWidth)
cv2.createTrackbar("Box Height","My Trackbars",10,dispH - 1,BoxHeight)
if not cap.isOpened():
    print("❌ Camera not opened")
    exit()

while True:
    ret, frame = cap.read()
    cv2.rectangle(frame,(xpos, ypos),(xpos+boxwidth, ypos+boxheight),(0,0,255),5)
    cv2.imshow("Camera",frame)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()


