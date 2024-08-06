# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:52:49 2024

@author: MUHARREM GEDİK
"""

#%% İmage Blurring

#importing libraries
import cv2
import numpy as np

image = cv2.imread(r"img1.png")

cv2.imshow("Original Image", image)
cv2.waitKey(0)

#Gaussion Blur
Gaussion_image = cv2.GaussianBlur(image, (7,7), 0)
cv2.imshow("Gaussion Blurring",Gaussion_image)
cv2.waitKey(0)

#Median Blur
Median_image = cv2.medianBlur(image,5)
cv2.imshow("Median Blurring",Median_image)
cv2.waitKey(0)

#Bilateral Blur
Bilateral_image = cv2.bilateralFilter(image,9,75,75)
cv2.imshow("Bilateral Blurring",Bilateral_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
