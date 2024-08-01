# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 16:31:43 2024

@author: MUHARREM GEDİK
"""

#%% cv2.imshow() explain

# Python program to explain cv2.imshow() method

# importing cv2
import cv2

# path
path = r'picture.jpg'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'ai_picture'

# Using cv2.imshow() method
# Displaying the image
cv2.imshow(window_name, image)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
