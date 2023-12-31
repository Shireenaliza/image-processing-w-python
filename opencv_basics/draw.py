import cv2
import numpy as np 
import matplotlib.pyplot as plt
import subprocess

#pure black img
blank_img = np.zeros(shape=(512,512,3),dtype=np.int16)

print(blank_img.shape)

'''
plt.imshow(blank_img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/blank_img.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/blank_img.jpeg'])
'''

#draw rectangle on img
#rectangle( img , tuple1 , tuple2) -- > t1 = top left vertex , t2 = bottom right
rec_img = cv2.rectangle(blank_img,pt1=(200,200),pt2=(300,300),color=(0,0,255),thickness=10)

print(cv2.rectangle(blank_img,pt1=(200,200),pt2=(300,300),color=(0,0,255),thickness=10))

plt.imshow(rec_img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/rec_img.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/rec_img.jpeg'])

