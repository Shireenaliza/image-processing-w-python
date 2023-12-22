import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image
import subprocess

pic = Image.open('/home/user/projects/image-processing-w-python/DATA/00-puppy.jpg')

pic_arr = np.asarray(pic)

pic_red = pic_arr.copy()

#GREEN CHANNEL 
print(pic_red[:,:,1])

#R G B
pic_red[:,:,1] = 0  #no green
pic_red[:,:,2] = 0  #no blue

print(pic_red.shape)  
print(pic_red[:,:,1].shape)

plt.imshow(pic_red)
plt.savefig('/home/user/projects/image-processing-w-python/DATA/displayed_red_image.png')
subprocess.run(['xdg-open', '/home/user/projects/image-processing-w-python/DATA/displayed_red_image.png'])


