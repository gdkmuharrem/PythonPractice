# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:06:11 2024

@author: MUHARREM GEDİK
"""

#%%  string

s = "bugün günlerden pazartesi"

variable_type = type(s) #str = string

print(s)

var1 = "ankara"
var2 = "ist"
var3 = var1+var2
print(var3)

var4 = "100"
var5 = "200"
var6 = var4+var5
print(var6)

uzunluk = len(var6)

var6[3] # 100200 içinden 3.indexi yani 4.karakteri alacak. 0-1-2-(3)

#Bir stringi bir sayıyla çarparsak o kadar concat işlemi yapar.
"Gedik"*3
