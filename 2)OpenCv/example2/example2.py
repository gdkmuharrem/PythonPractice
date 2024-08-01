# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:38:58 2024

@author: MUHARREM GEDİK
"""

#%% example2

#import cv2, numpy and matplotlib libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("geeksforgeeks.png")
#Displaying image using plt.imshow() method
plt.imshow(img)
 
#hold the window
plt.waitforbuttonpress()
plt.close('all')
