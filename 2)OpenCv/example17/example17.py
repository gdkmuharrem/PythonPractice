# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:46:01 2024

@author: MUHARREM GEDİK
"""

#%% Image Resizing

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r"img1.png",1)
half = cv2.resize(image, (0,0), fx=0.1, fy=0.1)
bigger = cv2.resize(image, (1050,1610))
stretch_near = cv2.resize(image, (780,540), interpolation = cv2.INTER_LINEAR)

Titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]
images = [image, half, bigger, stretch_near]
counter1 = 4

for i in range(counter1):
    plt.subplot(2, 2, i+1)
    plt.title(Titles[i])
    plt.imshow(images[i])

plt.show()
