import cv2 

img = cv2.imread('/home/user/Documents/projects/image-processing-w-python/Images/catto.jpeg')
fix_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#imshow( windowname , img)
cv2.imshow('kitty', fix_img)
cv2.waitKey()

#wait key -- have i waited atleast this many ms?

#or

while True:
    cv2.imshow('katto', fix_img)
    
    #if we waited atleast 1 ms AND  we pressed Esc Key
    if cv2.waitKey(1) & 0xFF == 27:
        break 
    
cv2.destroyAllWindows()


    