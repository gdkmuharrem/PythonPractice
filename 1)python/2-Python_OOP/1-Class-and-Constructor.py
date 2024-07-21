# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:49:17 2024

@author: MUHARREM GEDİK
"""

#%% Class and Constructor

class Calisan:
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim+soyisim+"@asd.com"

    def giveNameAndSurname(self):
        return self.isim + " " + self.soyisim        




isci1 = Calisan("ali","veli",1000)

print(isci1.isim)
print(isci1.soyisim)
print(isci1.maas)
print(isci1.email)

isci1.giveNameAndSurname()
