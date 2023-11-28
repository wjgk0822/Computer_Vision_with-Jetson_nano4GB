import cv2
import numpy as np

#def thresholding():
img=cv2.imread('download.jpeg',cv2.IMREAD_GRAYSCALE)

ret,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

ret,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,th3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('original',img) 

cv2.imshow('Bineary_Inv',th2)
cv2.imshow('Trunc',th2)
cv2.imshow('Tozero',th2)
cv2.imshow('Tozero_Inv',th2)

cv2.waitKey()



