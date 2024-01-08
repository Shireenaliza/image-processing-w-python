import cv2
import numpy as np
import matplotlib.pyplot as plt
import subprocess

img = cv2.imread("/home/user/Documents/projects/image-processing-w-python/Images/pretty_cat.jpeg")

fixed_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#while using plt and subprocess to display the image loaded by imread(0) do color correction BGR2RBG

if img is None:
    print("Error: Could not load the image")
    exit()
    
'''
while True:
    cv2.imshow('katto', img)

    if cv2.waitKey(1) & 0xFF == 27:
        break 

cv2.destroyAllWindows()
'''

#flip img
new_img = cv2.flip(fixed_img, 0)
'''plt.imshow(new_img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/flipped.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/flipped.jpeg'])
'''

#draw empty red box around face
img2 = cv2.imread("/home/user/Documents/projects/image-processing-w-python/Images/winter_cat.jpeg")
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

rec_img = cv2.rectangle(img2 ,pt1=(250,200),pt2=(450,390),color=(0,0,255),thickness=5)

plt.imshow(rec_img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/rec_img.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/rec_img.jpeg'])

