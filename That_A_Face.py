import cv2

trained_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('dafian.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Dafian', gray_img)
cv2.waitKey()

print("Lmao Complete")