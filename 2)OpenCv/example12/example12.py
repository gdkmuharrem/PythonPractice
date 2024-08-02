# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:58:21 2024

@author: MUHARREM GEDİK
"""

#%% Subtraction of Image:
    
# Python program to illustrate 
# arithmetic operation of 
# subtraction of pixels of two images 

# organizing imports 
import cv2 
import numpy as np 
	
# path to input images are specified and 
# images are loaded with imread command 
image1 = cv2.imread('img1.jpg') 
image2 = cv2.imread('img2.jpg') 

# cv2.subtract is applied over the 
# image inputs with applied parameters 
sub = cv2.subtract(image1, image2) 

# the window showing output image 
# with the subtracted image 
cv2.imshow('Subtracted Image', sub) 

# De-allocate any associated memory usage 
if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows() 
