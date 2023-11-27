#test6
import cv2 
import matplotlib.pyplot as plt 

imgBGR=cv2.imread('download.jpeg') 

imgGray=cv2.imread('download.jpeg',cv2.IMREAD_GRAYSCALE)



imgRGB=cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB)


#plt.axis('off')

#plt.imshow(imgGray,cmap='gray')

plt.subplot(121),plt.axis('off'),plt.imshow(imgRGB)

plt.subplot(122),plt.axis('off'),plt.imshow(imgGray,cmap='gray')





plt.show()


