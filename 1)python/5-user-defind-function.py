# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:38:27 2024

@author: MUHARREM GEDİK
"""

#%%  user defind functions

var1 = 10
var2 = 100
output1 = (((var1+var2)*50)/100.0)*var1/var2

var3 = 40
var4 = 60
output2 = (((var3+var4)*50)/100.0)*var3/var4

#yukarıdaki işlemi fonksiyon yazmazsak saatlerce tekrarlamak zorunda kalırdık.
#Aşağıda fonksiyon tanımlayarak işlemi kolaylaştırıcaz.

def benim_ilk_func(a,b):
    """
        Bu benim ilk function denemem.
        
        parametre: var1 ve var2
            
        return: output
            
    """
    output = (((a+b)*50)/100.0)*a/b
    return(output)

sonuc = benim_ilk_func(var1, var2)

def benim_ikinci_func():
    print("İkinci Function'a hoş geldiniz.")
