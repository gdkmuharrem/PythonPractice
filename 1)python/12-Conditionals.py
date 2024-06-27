# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 15:29:54 2024

@author: MUHARREM GEDİK
"""

#%% Conditionals

#İf-Else Statement

1==1 #True döndürür. 1, 1'e eşit mi?
1==2 #False döndürür. 1, 2'ye eşit mi?
1!=1 #False döndürür. 1, 1'e eşit değildir mi?
True == True
True == False
1>5  #False döner. 1, 5'den küçüktür.
5>5  #False döner. 5, 5'e eşittir.

1>0 and 4<5 #True döndürür. And(ve) ile Doğru+Doğru = Doğru
1>0 or 4<3 #True döndürür. Or(veya) ile Doğru ya da Yanlış = Doğru

#%%
var1 = 10
var2 = 20

if(var1 > var2):
    print("var1 buyuktur var2")
elif(var1 == var2):
    print("var1 eşittir var2.")
else:
    print("var1 küçüktür var2")

#%%
liste = [1,2,3,4,5,6]
value = 7
if value in liste:
    print("Evet {} değeri listede var.".format(value))
else:
    print("Hayır {} değeri listede yok.".format(value))

#%%
dic1 = {"ali":1,"veli":24,"memet":51}
keys = dic1.keys()
value = "memet"
if value in keys:
    print("Evet {} sözlükte var ve değeri {}".format(value,dic1[value]))
else:
    print("Hayır {} sözlükte yok.".format(value))
