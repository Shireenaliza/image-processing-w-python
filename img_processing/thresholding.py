#colored img --> binary img 
# 0-->BLACK  1-->WHITE

import cv2
import matplotlib.pyplot as plt
import subprocess

img = cv2.imread("/home/user/Documents/projects/image-processing-w-python/Images/rainbow.jpg",0) #,0 makes it grey scale img!


plt.imshow(img, cmap='grey')
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/task.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/task.jpeg'])

#thresholding --> any values below t turn to 0 , any values above it turn to MAX

#threshold(img , t , maxval, type of t)

#255/2 == 127.5

ret , thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY) #_INV

print(ret)

#display BINARY IMG
plt.imshow(thresh1, cmap='grey')
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/task1.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/task1.jpeg'])

#threshold truncation
#if src is above t, it's brought down to t
ret , thresh2 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC) #_TOZERO
plt.imshow(thresh2, cmap='grey')
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/task1.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/task1.jpeg'])


