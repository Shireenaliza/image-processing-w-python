import cv2
import numpy as np 
import matplotlib.pyplot as plt
import subprocess

#generate a black img/ blank image
blank_img = np.zeros(shape=(512,512,3),dtype=np.int16)

font = cv2.FONT_ITALIC
txt_img = cv2.putText( blank_img , text = 'hello world' , org =(10,500), fontFace= font , fontScale=3 , color=(255,255,255),thickness=3, lineType=cv2.LINE_AA)

plt.imshow(txt_img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/txt_img.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/txt_img.jpeg'])
