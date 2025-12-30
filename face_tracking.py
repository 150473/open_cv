import cv2
import time
fps = 0
cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier('./haar/haarcascade_frontalface_default.xml')
while True:
    starttime = time.time()
    ret, frame = cap.read()
    frameGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray,1.3,5)
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0,0),3)
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


