import cv2
import subprocess
import matplotlib.pyplot as plt


img = cv2.imread('/home/user/Documents/projects/image-processing-w-python/Images/catto.jpeg')
fix_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

print(fix_img.shape)

#resize (img , new dimentions) 
# size == (772, 735, 3) .... 1000~735 && 400~772
new_img = cv2.resize(fix_img,(1000,400))

plt.imshow(new_img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/catto_edit5.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/catto_edit5.jpeg'])

#reduce image by 50% ratio
w_ratio = 0.5
h_ratio = 0.5

new_img2 = cv2.resize(fix_img,(0,0),fix_img,w_ratio,h_ratio)

plt.imshow(new_img2)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/catto_edit6.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/catto_edit6.jpeg'])

print(new_img2.shape)