import numpy as np
import matplotlib.pyplot as plt
import subprocess

from PIL import Image

pic = Image.open('/home/user/projects/image-processing-w-python/DATA/00-puppy.jpg')

pic_arr = np.asarray(pic)

pic_red = pic_arr.copy()

# R G B
#pic_red[:,:,0] is for Red Channel

plt.imshow(pic_red[:,:,0])
plt.savefig('/home/user/projects/image-processing-w-python/DATA/displayed_red_image.png')
subprocess.run(['xdg-open', '/home/user/projects/image-processing-w-python/DATA/displayed_red_image.png'])


