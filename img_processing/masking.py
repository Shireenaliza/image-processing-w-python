#blend images of diff sizes

import cv2
import matplotlib.pyplot as plt
import subprocess

img1 = cv2.imread("/home/user/Documents/projects/image-processing-w-python/Images/tree_cat.jpeg")
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img1 = cv2.resize(img1, (1900,1900))

img2 = cv2.imread("/home/user/Documents/projects/image-processing-w-python/Images/watermark_no_copy.png")
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
img2 = cv2.resize(img2,(600,600))

print(img1.shape , img2.shape)

x_offset = 1900 - 600
y_offset = 1900 - 600

#set parameters as of the smaller img
rows,cols,channels = img2.shape

print(rows,cols,channels)

#region of interest
roi = img2[y_offset:1900, x_offset:1900]

#create the MASK 

img2grey = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
print("shape of roi",roi.shape)

'''
plt.imshow(img2grey,cmap='grey')
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/task.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/task.jpeg'])
'''

mask_inv = cv2.bitwise_not(img2grey)
print("mask inv shape:",mask_inv.shape)

'''
plt.imshow(mask_inv,cmap='grey')
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/task1.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/task1.jpeg'])
'''
#mask inverse no longer contains colour channels , use np to add it back

import numpy as np 

white_background = np.full(img2.shape,255,dtype=np.uint8)
print("white bg shape:",white_background.shape)

#every color channel will have img2
bk = cv2.bitwise_or(white_background,white_background,mask=mask_inv)
print(bk.shape)

#place original foreground image on top of mask
fg = cv2.bitwise_or(img2,img2,mask=mask_inv)

'''
plt.imshow(fg,cmap='grey')
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/task1.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/task1.jpeg'])
'''
#get roi and blend mask with it 
final_roi = cv2.bitwise_or(roi,fg)
'''
plt.imshow(final_roi)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/task1.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/task1.jpeg'])

'''
large_img = img1
small_img = final_roi

large_img[y_offset:y_offset+small_img.shape[0],x_offset:x_offset+small_img.shape[1]]= small_img

