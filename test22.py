import cv2
import numpy as np 

def tmpMatching(thr):
    img=cv2.imread('zidane.jpeg') 
    imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    template=cv2.imread('download.jpeg',cv2.IMREAD_GRAYSCALE) 
    
    w,h=template.shape[::-1] 
    res=cv2.matchTemplate(imgray,template,cv2.TM_CCOEFF_NORMED) 
    loc=np.where(res>=thr) 
    
    for pt in zip(*loc[::-1]):
        
        cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),2) 
    cv2.imshow('res',img) 
        
    cv2.waitKey(0) 
        
    cv2.destroyAllWindows() 
        
tmpMatching(0.8)

         
         
    
    