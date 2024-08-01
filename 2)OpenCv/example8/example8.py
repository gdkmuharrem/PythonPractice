# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 18:29:27 2024

@author: MUHARREM GEDİK
"""

#%% multiple images

import cv2

# Load images
image1 = cv2.imread('picture.jpg')
image2 = cv2.imread('picture1.jpg')

# Display images in different windows
cv2.imshow('AI_Img', image1)
cv2.imshow('Person_Img', image2)

cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close all OpenCV windows
