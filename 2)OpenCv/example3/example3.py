# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:40:16 2024

@author: MUHARREM GEDİK
"""

#%% Example 3

#import cv2, numpy and matplotlib libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("geeksforgeeks.png")
 
# Converting BGR color to RGB color format
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
#Displaying image using plt.imshow() method
plt.imshow(RGB_img)
 
# hold the window
plt.waitforbuttonpress()
plt.close('all')
