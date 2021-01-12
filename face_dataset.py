import cv2
import os



cam = cv2.VideoCapture(0) # camera id 0 means webcam. if you have more than one, replace 0 with your desire camera id
cam.set(3,640) #weidth
cam.set(4,480) #height
cam.set(10,100) #brightness


face_detector = cv2.CascadeClassifier('assets/haarcascade_frontalface_default.xml')
face_id = 1
# face_id = input('\nEnter user id: ')
print('\n [INFO] Initializing face capture.')


# higher means better 
numberOfImageCapture = 0

while True:
    rect, img = cam.read()
    # image detection works on gray images
    gray_img =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_img, 1.3,5)

    for (x,y, width, height) in faces:
        # (img, (start possition),(end Position), color, stroke)
        cv2.rectangle(img, (x,y), (x+width, y+height), (255,0,0),2)
        numberOfImageCapture+=1

        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(face_id) + ".jpg", gray_img[y:y+height,x:x+width])

        cv2.imshow('image', img)

    # capture time
    k = cv2.waitKey(100) & 0xff
    # waiting time 27 sec
    if k==27:
        break
    elif numberOfImageCapture>=30:
        break

print("\n[INFO] Exiting program")
cam.release()
cv2.destroyAllWindows()

