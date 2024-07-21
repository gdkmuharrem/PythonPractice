# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:39:29 2024

@author: MUHARREM GEDİK
"""

#%% QUİZ3

# Aşağıdaki listenin içerisindeki en küçük sayının ekrana basılmasını sağlayınız.
liste = [1,2,3,4,5,6,4,15,215,12,40,-215,-124,34,421]


#Çözüm:
#----------
a = 0
for each in liste:
    if (a > each):
        a = each
    else:
        continue
print (a)