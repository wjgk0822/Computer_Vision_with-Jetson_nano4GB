import cv2 
import numpy as np 

from PIL import Image 

import pytesseract 

filename='poem.png' 

img=np.array(Image.open(filename))

text=pytesseract.image_to_string(img)

print(text) 



