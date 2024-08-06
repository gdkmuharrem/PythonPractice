# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:35:07 2024

@author: MUHARREM GEDİK
"""

#%% How to main aspect ratio when resizing images ?

import cv2

#Load the image
image = cv2.imread(r"img1.png")

#Get the original dimesions
(h,w) = image.shape[:2]

#Desired width
new_width = 400

#Calculate aspect ratio
aspect_ratio = h/w
new_height = int(new_width*aspect_ratio)

#Resize the image
resized_image = cv2.resize(image,(new_width,new_height))

cv2.imshow('original image', image) 
cv2.imshow('resized image', resized_image) 

# De-allocate any associated memory usage 
if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows() 