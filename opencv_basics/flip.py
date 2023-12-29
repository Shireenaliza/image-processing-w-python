import matplotlib.pyplot as plt
import cv2
import subprocess

img = cv2.imread('/home/user/Documents/projects/image-processing-w-python/Images/catto.jpeg')
fix_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

new_img = cv2.flip(fix_img,0)   #horizontal axis

plt.imshow(new_img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/catto_edit6.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/catto_edit6.jpeg'])


new_img2 = cv2.flip(fix_img,1)   #vertical axis

plt.imshow(new_img2)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/catto_edit7.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/catto_edit7.jpeg'])

new_img3 = cv2.flip(fix_img,-1)   #vboth axis

plt.imshow(new_img3)
cv2.imwrite('/home/user/Documents/projects/image-processing-w-python/Images/catto_edit8.jpeg', new_img3)
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/catto_edit8.jpeg'])
z
