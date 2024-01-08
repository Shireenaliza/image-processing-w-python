import matplotlib.pyplot as plt
import cv2
import subprocess

img = cv2.imread('/home/user/Documents/projects/image-processing-w-python/Images/catto.jpeg')

img_grey = cv2.imread('/home/user/Documents/projects/image-processing-w-python/Images/catto.jpeg',cv2.IMREAD_GRAYSCALE)

plt.imshow(img_grey)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/catto_edit3.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/catto_edit3.jpeg'])

print(img_grey.shape)
print(img_grey.min(), img_grey.max())

plt.imshow(img_grey, cmap ='gray')
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/catto_edit4.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/catto_edit4.jpeg'])
