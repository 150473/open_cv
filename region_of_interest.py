import cv2
import time
cap = cv2.VideoCapture(0)
dispW = 1920
dispH = 1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

if not cap.isOpened():
    print("❌ Camera not opened")
    exit()

while True:
    ret, frame = cap.read()
    frame[:int(dispH/2),:int(dispW/2)] = [0,0,255]
    frame[int(dispH/2):,:int(dispW/2)] = [255,0,0]
    frame[:int(dispH/2),int(dispW/2):] = [0,255,0]
    frame[int(dispH/2):,int(dispW/2):] = [255,255,0]
    cv2.imshow("Camera",frame)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()


