import cv2
import time
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.rectangle(frame,(250,50),(350,125),(0,0,255),3)
    cv2.imshow("Camera",frame)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()


