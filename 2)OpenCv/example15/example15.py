# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:44:05 2024

@author: MUHARREM GEDİK
"""

#%% Bitwise XOR operation on image

# Python program to illustrate 
# arithmetic operation of 
# bitwise XOR of two images 
	
# organizing imports 
import cv2 
import numpy as np 
	
# path to input images are specified and 
# images are loaded with imread command 
img1 = cv2.imread('img1.png') 
img2 = cv2.imread('img2.png') 

# cv2.bitwise_xor is applied over the 
# image inputs with applied parameters 
dest_xor = cv2.bitwise_xor(img1, img2, mask = None) 

# the window showing output image 
# with the Bitwise XOR operation 
# on the input images 
cv2.imshow('Bitwise XOR', dest_xor) 

# De-allocate any associated memory usage 
if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows() 
