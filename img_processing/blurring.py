#done before applying EDGE DETECTION ALGOS

#gamma correction --> brightness set acc to gamma value chosen
#kernels -- applied to images to produce variety of images 

import cv2
import matplotlib.pyplot as plt
import subprocess
import numpy as np 

def load_img():
    img = cv2.imread("/home/user/Documents/projects/image-processing-w-python/Images/bricks.jpg").astype(np.float32) / 255
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img

def display_img(img):
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='grey')
    plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/brickwall.jpeg')
    subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/brickwall.jpeg'])

i = load_img()
display_img(i)

#gamma correction 
#gamma<1 -- brightness inc , gamma>1 -- darker
gamma = 1/4
result = np.power(i,gamma) #akes every pixel value of img and raises it to the power of gamma
#display_img(result)   

#low pass filter w 2D Convolution (a blurring)
font = cv2.FONT_HERSHEY_SIMPLEX
text_img = cv2.putText(i,text='bricks',org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)
display_img(text_img)
