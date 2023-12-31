import cv2
import numpy as np

#function
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,255,0),-1)
    
         
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,0,255),-1)

cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing',draw_circle)

#showing image /w open cv
img = np.zeros((512,512,3),np.int8)  #remove np.int8 to get black bg

while True:
    cv2.imshow('my_drawing',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
