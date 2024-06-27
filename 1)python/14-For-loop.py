# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:55:54 2024

@author: MUHARREM GEDİK
"""

#%% For loop

#range(x,y) => x dahil y hariç olacak şekilde aralıktaki tüm sayılar ile bir liste oluşturur.
#split() => stringlerin arasındaki boşluğa göre ayırmaya yarar.
#sum(x) => x'deki herşeyi toplar.

#for loop syntax:
for a in range(1,11):
    print(a)
    
for a in "ankara ist":
    print(a)
    
for a in "ankara ist".split():
    print(a)

liste = [1,2,3,4,2,4,6,7,4,5,6,12]
summation = sum(liste)

count = 0
for a in liste:
    count = count+a
    print(count)






