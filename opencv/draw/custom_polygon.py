import cv2
import numpy as np 
import matplotlib.pyplot as plt
import subprocess

#generate a black img/ blank image
blank_img = np.zeros(shape=(512,512,3),dtype=np.int32)

plt.imshow(blank_img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/blank_img.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/blank_img.jpeg'])


#decide the vertices
vertices = np.array([[100,400],[300,100],[500,200]], dtype=np.int32)
print(vertices)

print(vertices.shape) #images need to be in 3 dimentions 

#adds a third dimention '1' in the middle - reshape the vetives then pass them in as a list 
pts = vertices.reshape((-1,1,2))  
print(pts.shape)

poly_img = cv2.polylines(blank_img,[pts],isClosed=True, color=(255,0,0),thickness=2)

plt.imshow(poly_img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/poly_img.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/poly_img.jpeg'])

#fill poly
polyfilled_img = cv2.fillPoly(blank_img,[pts],color=(255,0,0))

plt.imshow(poly_img)
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/task2.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/task2.jpeg'])
