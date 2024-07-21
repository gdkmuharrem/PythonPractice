# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:40:37 2024

@author: MUHARREM GEDİK
"""

#%%  Quiz 1
#int variable = yas
#string name = isim
#function = print(type(),len,float())
#*args soyisim
#default ayakkabi no

yas = 10
name = "Muharrem"
surname = "Gedik"

def functionQuiz(yas,name,*args,ayakkabiNo=35):
    print("Çocuğun ismi : ",name,args[0],"\nÇocuğun yaşı : ",yas,"\nÇocuğun ayakkabi numarası : ",ayakkabiNo)
    print(args[0]*8)
    
functionQuiz(yas, name, surname)
