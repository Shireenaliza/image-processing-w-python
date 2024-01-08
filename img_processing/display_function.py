import cv2
import matplotlib.pyplot as plt
import subprocess

img = cv2.imread("/home/user/Documents/projects/image-processing-w-python/Images/crossword.jpg",0)

plt.imshow(img, cmap='grey')
plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/task.jpeg')
subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/task.jpeg'])

#function to display image bigger
def show_pic(img):
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='grey')
    plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/task.jpeg')
    subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/task.jpeg'])

show_pic(img)