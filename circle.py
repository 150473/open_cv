import cv2
import time
cap = cv2.VideoCapture(0)
dispW = 1280
dispH = 720
cap.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

if not cap.isOpened():
    print("❌ Camera not opened")
    exit()

while True:
    ret, frame = cap.read()
    cv2.circle(frame,(640,320),50,(0,0,255),3)
    cv2.imshow("Camera",frame)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()


