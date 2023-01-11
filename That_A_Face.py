import cv2

trained_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('dafian.png')
cv2.imshow('Dafian', img)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.waitKey()

print("Lmao Complete")