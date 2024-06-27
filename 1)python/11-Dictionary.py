# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 15:24:04 2024

@author: MUHARREM GEDİK
"""

#%%  Dictionary (sözlük)

dict1 = {"ali":32,"veli":45,"ayse":13}

dict1["ali"]
type(dict1["ali"])

#ali,veli,ayse =>> keys
#32,45,13 =>> values

dict1.keys() # keyleri verir.
dict1.values() # valueleri verir.


def deneme():
    dict1 = {"ali":13,"veli":41,"ayse":21412}
    return dict1

dict2 = deneme()

