import numpy as np 

arr = np.ones((5,5))
print(arr*10)

#SEED are used to generate the same random numbers every time

np.random.seed(101)
arr1 = np.random.randint(low=0,high=100,size=(5,5))
print(arr1)

print(arr1.max(), arr1.min())

#use PIL & matplotlib to display pic 
import matplotlib.pyplot as plt
from PIL import Image
import subprocess

pic = Image.open('/home/user/Documents/projects/image-processing-w-python/DATA/00-puppy.jpg')
plt.imshow(pic)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/DATA/00-puppy.jpg')
subprocess.run(['xdg-open','/home/user/Documents/projects/image-processing-w-python/DATA/00-puppy.jpg'])

print(type(pic))

#convet image to a numpy array
arr2 = np.asarray(pic)

print(type(arr2))
print(arr2.shape)

#use slicing to set R G Channels to zero & show isolated B Channel
mycopy = arr2.copy()

mycopy[:,:,0] = 0 
mycopy[:,:,1] = 0



plt.imshow(mycopy)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/DATA/blue_pic.jpg')

subprocess.run(['xdg-open','/home/user/Documents/projects/image-processing-w-python/DATA/blue_pic.jpg'])
