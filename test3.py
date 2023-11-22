#test3

import cv2 
import nanocamera as nano 

if __name__=='__main__':
    camera=nano.Camera(flip=2,width=640,height=480,fps=30) 
    
    print("CSI camera ready?: ",camera.isReady())
    
while camera.isReady():
    try:
        frame=camera.read()
        cv2.imshow("Video Frame",frame)
        if cv2.waitKey(25) & 0xFF==ord('q'):
            break 
    except KeyboardInterrupt:
        break 
    
camera.release()
del camera



    
