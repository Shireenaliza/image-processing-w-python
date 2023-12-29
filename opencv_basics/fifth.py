#save a file 

import cv2
import matplotlib.pyplot as plt
import subprocess

img = cv2.imread('/home/user/Documents/projects/image-processing-w-python/Images/catto.jpeg')
fix_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

print(type(fix_img))

cv2.imwrite('totally_new_img.jpg',fix_img)