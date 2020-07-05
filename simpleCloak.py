
import cv2 
import numpy as np 
import time 
from pygame import mixer  # Load the popular external library

mixer.init()
mixer.music.load('harry-potter-theme.mp3')
mixer.music.play()


capture_video = cv2.VideoCapture(0) 
     
# camera takes a second to warm up 
time.sleep(1)  

background = 0 
  
# capturing the background for some frames 

for i in range(60): 
    return_val, background = capture_video.read() 
    if return_val == False : 
        continue 
  

while True: 
    return_val, frame = capture_video.read() 
    if not return_val : 
        break 
  
    # converting BGR to HSV for better capture of hues
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  
  
    # setting the lower and upper range for mask1 
    lower_red = np.array([100, 40, 40])        
    upper_red = np.array([100, 255, 255]) 

    mask1 = cv2.inRange(hsv, lower_red, upper_red) 
    # setting the lower and upper range for mask2  
    lower_red = np.array([155, 40, 40]) 
    upper_red = np.array([180, 255, 255]) 

    mask2 = cv2.inRange(hsv, lower_red, upper_red) 
  
    mask1 = mask1 + mask2 
  
    # Refining the mask using morphing functions 

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((5, 5), 
                                         np.uint8), iterations = 2) 
    mask1 = cv2.dilate(mask1, np.ones((5, 5), np.uint8), iterations = 1) 

    mask2 = cv2.bitwise_not(mask1) 
  
    # final output 
    res1 = cv2.bitwise_and(background, background, mask = mask1) 
    res2 = cv2.bitwise_and(frame, frame, mask = mask2) 
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0) 
  
    cv2.imshow("MY CLOAK", final_output) 
    if cv2.waitKey(1) and  0xFF == ord('q'):
        break
