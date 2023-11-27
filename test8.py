import cv2
import numpy as np

img=np.full((400,400,3),255,np.uint8)

cv2.line(img,(50,50),(200,50),(0,255,255),10)
cv2.line(img,(50,60),(150,160),(255,0,0),5) 

cv2.rectangle(img,(50,200,150,200),(0,255,0),2)
cv2.rectangle(img,(70,220),(180,200),(0,128,0),-1)

cv2.circle(img,(300,100),30,(255,0,0),-1)
cv2.circle(img,(300,100),60,(0,200,0),3)

point=np.array([[250,200],[300,200],[350,300],[250,300]])
cv2.polylines(img,[point],True,(0,0,200),2)

text='Hello World !'

cv2.putText(img,text,(50,350),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,20,0),1)


cv2.imshow('img',img) 

cv2.waitKey() 

cv2.destroyAllWindows()



