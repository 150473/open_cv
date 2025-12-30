import cv2
import time
fps = 0
cap = cv2.VideoCapture(0)
while True:
    starttime = time.time()
    ret, frame = cap.read()
    cv2.putText(frame,str(int(fps)) +" fps",(30,60),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,255),3)
    cv2.imshow("Camera",frame)
    if cv2.waitKey(1) == 27:
        break
    endtime = time.time()
    looptime = endtime - starttime
    fps = 1/looptime
    #print(int(fps))
cap.release()
cv2.destroyAllWindows()


