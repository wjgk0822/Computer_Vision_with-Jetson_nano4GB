#test5
import cv2 

img=cv2.imread('download.jpeg',cv2.IMREAD_GRAYSCALE)

cv2.imwrite('dog_gray.jpg',img)


if img is None:
    print("Image load failed")
    exit()
    
    
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.moveWindow('image',600,200)
cv2.resizeWindow('image',200,500)

cv2.imshow("image",img)
cv2.waitKey(2000)
#cv2.destroyAllWindows()

while True:
    if cv2.waitKey()==27:#ord('q'):
        break 
    

#27 ESC,13 ENTER,9 TAB 

cv2.destroyAllWindows()




 


