import cv2
img=cv2.imread('.dist/car.png',-1)
img=cv2.resize(img,(400,400))
print(img)
cv2.imshow('IMAGE',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
