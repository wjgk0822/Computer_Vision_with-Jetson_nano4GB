import cv2
import numpy as np

def bluring():
    img=cv2.imread('download.jpeg')
    
    imgblu=np.ones((5,5),np.float32)/25
    blur=cv2.filter2D(img,-1,imgblu)
    
    cv2.imshow('original',img) 
    cv2.imshow('blur',blur)
    
    cv2.waitKey()
    cv2.destroyAllWindows()
    
bluring()


    
    