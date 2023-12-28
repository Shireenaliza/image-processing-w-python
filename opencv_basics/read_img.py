import numpy as np 
import matplotlib.pyplot as plt
import subprocess

import cv2

img = cv2.imread('/home/user/Documents/projects/image-processing-w-python/Images/catto.jpeg')
print(type(img))

#imread() reads directly as an array
#id type == None , path is incorrect

plt.imshow(img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/catto_edit.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/catto_edit.jpeg'])

#MATPLOTLI --- R G B
#OPENCV --- B G R

fix_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(fix_img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/catto_edit2.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/catto_edit2.jpeg'])
