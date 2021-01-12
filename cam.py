import cv2
import os



cam = cv2.VideoCapture(0) # camera id 0 means webcam. if you have more than one, replace 0 with your desire camera id
cam.set(3,640) #weidth
cam.set(4,480) #height
cam.set(10,100) #brightness



while True:
    rect, img = cam.read()
    cv2.imshow('image : ', img)

# capture time
    k = cv2.waitKey(100) & 0xff

cam.release()
cv2.destroyAllWindows()