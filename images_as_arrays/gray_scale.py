import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image
import subprocess

pic = Image.open('/home/user/projects/image-processing-w-python/DATA/00-puppy.jpg')

pic_arr = np.asarray(pic)

pic_red = pic_green = pic_blue = pic_arr.copy()

#R G B
# RED CHANNEL VALUES 0-255
# 0-no colour val , 255- full colour
# for red 0-no red/pure black && 255-full pure red
plt.imshow(pic_red[:,:,0], cmap='gray')
plt.savefig('/home/user/projects/image-processing-w-python/DATA/displayed_red_image.png')
subprocess.run(['xdg-open', '/home/user/projects/image-processing-w-python/DATA/displayed_red_image.png'])

# GREEN CHANNEL VALUES 0-255
plt.imshow(pic_green[:,:,1], cmap='gray')
plt.savefig('/home/user/projects/image-processing-w-python/DATA/displayed_green_image.png')
subprocess.run(['xdg-open', '/home/user/projects/image-processing-w-python/DATA/displayed_green_image.png'])

# BLUE CHANNEL VALUES 0-255
plt.imshow(pic_blue[:,:,1], cmap='gray')
plt.savefig('/home/user/projects/image-processing-w-python/DATA/displayed_blue_image.png')
subprocess.run(['xdg-open', '/home/user/projects/image-processing-w-python/DATA/displayed_blue_image.png'])
