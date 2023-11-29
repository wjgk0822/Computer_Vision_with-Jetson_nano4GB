import cv2
import numpy as np

def tracking():
    try:
        print('camera open')
        cap=cv2.VideoCapture(1,cv2.CAP_V4L2)
        cap.set(3,640)
        cap.set(4,480)
    except:
        print('camera failed') 
        return
        
    while True:
        ret,frame=cap.read()
        
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        
        lower_blue=np.array([110,110,100]) 
        
        upper_blue=np.array([130,255,255]) 
        
        lower_green=np.array([50,100,100]) 
        
        upper_green=np.array([75,255,255]) 
        
        lower_red=np.array([-10,100,100]) 
        
        upper_red=np.array([10,255,255])
        
        mask_blue=cv2.inRange(hsv,lower_blue,upper_blue)
        
        mask_green=cv2.inRange(hsv,lower_green,upper_green)
        
        mask_red=cv2.inRange(hsv,lower_red,upper_red) 
        
        
        res1=cv2.bitwise_and(frame,frame,mask=mask_blue)
        
        res2=cv2.bitwise_and(frame,frame,mask=mask_green)
        
        res3=cv2.bitwise_and(frame,frame,mask=mask_red)
        
        
        
        cv2.imshow('original',frame)
        cv2.imshow('blue',res1)
        cv2.imshow('green',res2)
        cv2.imshow('red',res3) 
        
        
        k=cv2.waitKey(1) & 0xFF
        if k==27:
            
            break
    cv2.destroyAllWindows()
        
        
tracking()
        
        
        
         
        
        