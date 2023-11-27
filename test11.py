import cv2

img=cv2.imread('download.jpeg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('image',img)

for sigma in range(1,4):
    dst=cv2.GaussianBlur(img,(0,0),sigma)
    
    desc='sigma={}'.format(sigma)
    cv2.putText(dst,desc,(10,30),cv2.FONT_HERSHEY_SIMPLEX,1.0,255,1,cv2.LINE_AA)
    
    cv2.imshow('dst',dst)
    cv2.waitKey()
    
cv2.destroyAllWindows()

