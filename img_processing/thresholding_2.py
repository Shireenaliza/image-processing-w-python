import cv2
import matplotlib.pyplot as plt
import subprocess

img = cv2.imread("/home/user/Documents/projects/image-processing-w-python/Images/crossword.jpg",0)

#function to display image bigger
def show_pic(img):
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='grey')
    plt.savefig('/home/user/Documents/projects/image-processing-w-python/Images/task.jpeg')
    subprocess.run(['xdg-open', '/home/user/Documents/projects/image-processing-w-python/Images/task.jpeg'])

#SIMPLE BINARY THRESHOLD

ret,thresh1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
#show_pic(thresh1)

#ADAPTIVE THRESHOLD (img,maxval,adaptive methods,t type,block size,const)  block type-->odd no. 
thresh2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
#show_pic(thresh2)

#blend 2 thresholds

blended = cv2.addWeighted(src1=thresh1,alpha=0.6,src2=thresh2,beta=0.4,gamma=0)
show_pic(blended)