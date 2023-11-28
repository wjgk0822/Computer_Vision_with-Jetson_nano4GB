import cv2
import numpy as np 

def threshold():
    img=cv2.imread('download.jpeg',cv2.IMREAD_GRAYSCALE)
    
    ret,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY,11,2)
    
    th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY,11,2)
    
    titles=['Original','Global Thres','ADA_MEAN','ADA_GAUSIAN']
    
    images=[img,th1,th2,th3]
    
    for i in range(4):
        cv2.imshow(titles[i],images[i])
        
    cv2.waitKey()
    cv2.destroyAllWindows()
    
threshold()
    
        
    
    
    
    
    