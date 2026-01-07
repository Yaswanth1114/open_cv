import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
face = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        gray = gray[y:y+w, x:x+w]
        color = frame[y:y+h, x:x+w]
        eyes = eye.detectMultiScale(gray, 1.3, 5)
        for ex, ey, ew, eh in eyes:
            cv.rectangle(color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()