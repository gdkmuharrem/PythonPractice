# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:39:24 2024

@author: MUHARREM GEDİK
"""

#%%  lambda function (Daha hızlı fonksiyon yazmak için)

#Normal Bir Fonksiyon:
def hesapla(x):
    return x*x
sonuc1 = hesapla(3)

#Lambda fonksiyon:
sonuc2 = lambda x: x*x    #Tek satırda.
print(sonuc2(3))
