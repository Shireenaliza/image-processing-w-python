#Blending images using addWeighted func.

#formula to blend imgs,
# new_pixel = alph.pixel1 + beta.pixel2 +g amma

import cv2
import matplotlib.pyplot as plt
import subprocess

img1 = cv2.imread("/home/user/Documents/projects/image-processing-w-python/Images/tree_cat.jpeg")
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)


img2 = cv2.imread("/home/user/Documents/projects/image-processing-w-python/Images/watermark_no_copy.png")
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

#print(fixed1.shape , fixed2.shape)

#blending images of same size
re_img1 = cv2.resize(img1,(1200,1200))
re_img2 = cv2.resize(img2,(1200,1200))

'''                
plt.imshow(re_img1)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/task.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/task.jpeg'])

plt.imshow(re_img2)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/task1.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/task1.jpeg'])
'''

#addWeighted( src1,alpha,src2,beta,gamma)
blended = cv2.addWeighted(src1=re_img1,alpha=0.5,src2=re_img2,beta=0.5,gamma=0)

plt.imshow(blended)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/task2.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/task2.jpeg'])

#overlay small image on top of larger image (no blending)
#numpy reassignment /numpy slicing

'''
plt.imshow(img1)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/task2.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/task2.jpeg'])


plt.imshow(img2)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/task3.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/task3.jpeg'])
'''
small_img = img1
large_img = img2

x_offset = 0  #lop left corner
y_offset = 0

x_end = x_offset + small_img.shape[1]
y_end = y_offset + small_img.shape[0] 

# y values --> rows , x values --> col.

large_img[y_offset:y_end,x_offset:x_end] = small_img #replacing pixels of big img

plt.imshow(large_img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/task3.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/task3.jpeg'])

