import cv2
import numpy as np

vid = cv2.VideoCapture(0)
vid.set(3,640) 
vid.set(4,480) 
vid.set(10,100)

while True:
    success, img = vid.read()
    cv2.imshow("my image",img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
    cv2.imshow("my hsv",hsv)
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow("my mask",mask)
    cv2.imshow("my final",res)

    if cv2.waitKey(1) and  0xFF == ord('q'):
        break