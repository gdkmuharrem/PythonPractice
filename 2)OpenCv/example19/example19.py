# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:46:10 2024

@author: MUHARREM GEDİK
"""

#%% cv2.erode method example.

#importing cv2,numpy
import cv2
import numpy as np

#reading image
image = cv2.imread(r"img1.png")

#window name in which image is displayed.
window_name1 = "Image1"
window_name2 = "Image2"

#Creating kernels
kernel1 = np.ones((5,5),np.uint8)
kernel2 = np.ones((6,6),np.uint8)

#Using cv2.erode() method
last_image1 = cv2.erode(image,kernel1)
last_image2 = cv2.erode(image,kernel2,cv2.BORDER_REFLECT)

#Displaying the image
cv2.imshow(window_name1,last_image1)
cv2.imshow(window_name2,last_image2)

# De-allocate any associated memory usage 
if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows() 