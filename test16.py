import cv2 
import numpy as np 

def onMouse(x):
    pass 

def bluring():
    img=cv2.imread('download.jpeg')
    cv2.namedWindow('BlurImage')
    cv2.createTrackbar('Blur_Mode','BlurImage',0,2,onMouse)
    
    cv2.createTrackbar('BLUR','BlurImage',0,5,onMouse)
    
    mode=cv2.getTrackbarPos('Blur_Mode','BlurImage')
    val=cv2.getTrackbarPos('BLUR','BlurImage')
    
    while True:
        val=val*2+1 
        
        try:
            if mode==0:
                blur=cv2.blur(img,(val,val))
                
            elif mode==1:
                blur=cv2.GaussianBlur(img,(val,val),0)
                
            elif mode==2:
                blur=cv2.medianBlur(img,val)
                
            else:
                break
            
            cv2.imshow('BlurImage',blur)
                
                
        except:
            break
                
    
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    
        k=cv2.waitKey(1) & 0xFF
        if k==27:
            
            break
        
        mode=cv2.getTrackbarPos('Blur_Mode','BlurImage')
        
        val=cv2.getTrackbarPos('BLUR','BlurImage')
        
    cv2.destroyAllWindows()
bluring()


#bluring()


