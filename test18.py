import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

def canny():
    img=cv2.imread('download.jpeg',cv2.IMREAD_GRAYSCALE)
    
    edge1=cv2.Canny(img,50,300)
    
    edge2=cv2.Canny(img,100,300)
    
    edge3=cv2.Canny(img,170,300)
    
    cv2.imshow('Original',img) 
    
    cv2.imshow('Canny Edge1',edge1)
    cv2.imshow('Canny Edge2',edge2)
    cv2.imshow('Canny Edge3',edge3) 
    
    cv2.waitKey()
    
    cv2.destroyAllWindows()
    
canny()


    