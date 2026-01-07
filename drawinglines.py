import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    width=int(cap.get(3))
    heigth=int(cap.get(4))
    img=cv2.line(frame,(0,0),(width,heigth),(255,255,255),3)
    img=cv2.rectangle(img,(300,300),(400,400),(128,129,126),-1)
    cv2.imshow('live camera',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

