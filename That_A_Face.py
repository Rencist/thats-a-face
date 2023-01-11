import cv2

trained_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('dafian.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_coordinates = trained_face.detectMultiScale(gray_img)
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
print(face_coordinates)

cv2.imshow('Dafian', img)
cv2.waitKey()

print("Lmao Complete")