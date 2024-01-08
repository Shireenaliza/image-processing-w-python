#HSL - Hue Saturation Lightness
#HSV -  Hue Saturation Value

#how to convert to HSL HSV colour spaces

import cv2
import matplotlib.pyplot as plt
import subprocess

img = cv2.imread("/home/user/Documents/projects/image-processing-w-python/Images/winter_cat.jpeg")
fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

'''
plt.imshow(fix_img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/img.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/img.jpeg'])
'''

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)

plt.imshow(hsv_img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/img.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/img.jpeg'])


hls_img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

plt.imshow(hls_img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/img.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/img.jpeg'])
