# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 18:24:31 2024

@author: MUHARREM GEDİK
"""

#%% Class Example

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
        

calisan1 = Calisan("ahmet", "gedik", 1500)
calisan2 = Calisan("muharrem","gedik",3000)
calisan3 = Calisan("yunus", "emre", 3500)
calisan4 = Calisan("mehmet", "yıldız", 4500)

calisanListe = [calisan1,calisan2,calisan3,calisan4]

maxiMaas = 0
for each in calisanListe:
    if(each.maas>maxiMaas):
        maxiMaas = each.maas
        indexex = each # En yüksek maaş alan kişinin indexi.

print(maxiMaas)
print(indexex.giveNameAndSurname()) # En yüksek maaş alan kişinin adını soyadını ekrana basıyoruz.