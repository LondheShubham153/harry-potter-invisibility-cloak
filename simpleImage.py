import cv2

path = './images/newironman2.png'
image = cv2.imread(path)
img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("newiron",img_gray)
cv2.waitKey(0)