import cv2
import numpy as np

img=np.full((400,400,3),255,np.uint8)

cv2.line(img,(50,50),(200,50),5)
cv2.line(img,(50,60),(150,160),5) 

cv2.imshow('img',img) 

cv2.waitKey() 

cv2.destroyAllWindows()

 

