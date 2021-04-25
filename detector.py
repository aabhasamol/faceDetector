import cv2, glob

all_images = glob.glob("*.jpg") 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

 
for image in all_images:
    img = cv2.imread(image)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, 1.1, 5)

    for (x, y, w, h) in faces:
        final_img = cv2.rectangle(img, (x,y), (x+w,y+h), (0, 255, 255), 2)

    cv2.imshow("Face Detection", final_img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows
