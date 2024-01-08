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

#display image matrix?
#print(cv2.rectangle(blank_img,pt1=(200,200),pt2=(300,300),color=(0,0,255),thickness=10))

plt.imshow(rec_img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/rec_img.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/rec_img.jpeg'])

#draw a circle on img
#circle ( img , tuple1 , radius , colour , thickness) t1-->center of circle

circle_img = cv2.circle(img = blank_img , center = (100,100), radius = 50 , color = (255 , 0 , 100), thickness= 4)
plt.imshow(circle_img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/circle_img.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/circle_img.jpeg'])

# thickness = -1 --> filled circle

line_img = cv2.line(img=blank_img , pt1 = (0,0), pt2 = (512,512), color = (255,100,100), thickness = 5)
plt.imshow(line_img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/line_img.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/line_img.jpeg'])


