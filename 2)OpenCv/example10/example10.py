# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 14:49:24 2024

@author: MUHARREM GEDİK
"""

#%% Visualizing the different color channels of an RGB image. 


import cv2 
  
image = cv2.imread('img1.png') 
B, G, R = cv2.split(image) 
# Corresponding channels are separated 
  
cv2.imshow("original", image) 
cv2.waitKey(0) 
  
cv2.imshow("blue", B) 
cv2.waitKey(0) 
  
cv2.imshow("Green", G) 
cv2.waitKey(0) 
  
cv2.imshow("red", R) 
cv2.waitKey(0) 
  
cv2.destroyAllWindows() 
