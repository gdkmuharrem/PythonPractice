# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:41:30 2024

@author: MUHARREM GEDİK
"""

#%%  List

#Biz şimdiye kadar aşağıdaki gibi tek tek değişken tanımlamıştık.
var1 = 10
var2 = 20
var3 = 30 


#Şimdi sırada liste yapmaya başlayacağız.
#syntax'i aşağıdaki gibi köşeli parantezle yapılmakta.
liste = [1,2,3,4,5,6]
type(liste)

liste_str = ["pazartesi","salı","çarşamba"]
type(liste_str)


#Yukarıda liste oluşturduk. Şimdi ise içerisinden elemanlara erişicez.
value = liste[2] # 3 döndürmesi gerekmekte. Saymaya 0'dan başlamaktayız.
print(value)

value2 = liste_str[2] # çarşamba döndürmesi gerekmekte.
print(value2)

lastvalue = liste[-1] # index yerine -1 verirsek son elemanı döndürür.
print(lastvalue)

liste_divide = liste[0:3] # 0.index dahil olarak başlayıp 3.indexe kadar hepsini alır.
print(liste_divide)


#%%

### (dir) komutu ile bir metodun özelliklerini öğrenebiliriz.
dir(liste)
### help komutu ile detaylı bilgi alabiliriz.
help(list.append)

#%%

liste.append(7) #listenin sonuna 7 elemanını ekler.
liste.remove(7) #listeden 7 elemanını siler. Birden fazla varsa bir tanesini siler.
liste.reverse() #listeyi ters çevirir.

liste2 = [1,5,4,2,3,1,24,5]
liste2.sort() #listenin içindekileri küçükten büyüğe sıralar.

liste3 = [1,5,7,6,"aa","bb","aabb"] #hem int hem string liste oluşturduk.
liste3.sort()

