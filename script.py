import cv2
 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
photo = cv2.VideoCapture("ashu.jpg")
 
res, img = photo.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# Detects faces of different sizes in the input image
faces = face_cascade.detectMultiScale(gray, 1.01, 5)
 
for (x,y,w,h) in faces:
        # To draw a rectangle in a face
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
 
cv2.imshow('img',img)
k = cv2.waitKey(0)
 
# Close the window
photo.release()
 
# De-allocate any associated memory usage
cv2.destroyAllWindows()