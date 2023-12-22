import numpy as np
import matplotlib.pyplot as plt
import subprocess

from PIL import Image

pic = Image.open('/home/user/projects/image-processing-w-python/DATA/00-puppy.jpg')


plt.imshow(pic)

# Save the figure as an image file
plt.savefig('/home/user/projects/image-processing-w-python/DATA/displayed_image.png')

# Show the saved image using an external viewer 
subprocess.run(['xdg-open', '/home/user/projects/image-processing-w-python/DATA/displayed_image.png'])


print(type(pic_arr))
