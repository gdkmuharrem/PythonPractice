# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 18:06:45 2024

@author: MUHARREM GEDİK
"""

#%% Class Variable

class Calisan:
    
    sabitZamOrani = 1.8
    counter = 0
    
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim+soyisim+"@asd.com"
        
        Calisan.counter = Calisan.counter + 1  # Bu kod sayesinde her yeni bir çalışan eklendiğinde sayaç artacak.
        # Kaç çalışan olduğu tek bir değişkende saklanabilecek.
        # Bu değişkenlerde self yerine Class ismi kullanma sebebimiz tüm class için geçerli bir sayaç olmasıdır.
        
    def giveNameAndSurname(self):
        return self.isim + " " + self.soyisim
    
    def zamYap(self,zamOrani):
        self.maas = self.maas + self.maas*zamOrani
        
    def sabitZamYap(self):
        self.maas = self.maas + self.maas*self.sabitZamOrani
    
calisan1 = Calisan("ahmet", "gedik", 5880)
print(calisan1.isim," ",calisan1.soyisim," İlk maaş : ",calisan1.maas)

calisan1.sabitZamYap()
print(calisan1.isim," ",calisan1.soyisim," Sabit zamlı hali : ",calisan1.maas)

print(" /n")

calisan2 = Calisan("muharrem", "gedik", 6304)
print(calisan2.isim," ",calisan2.soyisim," İlk maaş : ",calisan2.maas)

calisan2.zamYap(1.9)
print(calisan2.isim," ",calisan2.soyisim," Zamlı hali : ",calisan2.maas)