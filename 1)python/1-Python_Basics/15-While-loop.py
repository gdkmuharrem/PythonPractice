# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:34:18 2024

@author: MUHARREM GEDİK
"""

#%% While Loop

i = 0
while i<4:
    print(i)
    i = i + 1



## Aşağıdaki örnekte listenin içerisindekileri tamamen toplama işlemi yaptık.
## For loop ile benzer işlevi daha kıssa yapabilirdik fakat hepsinin kullanım alanları farklı.

ornekListe = [1,2,3,4,5,6,7,8,9,1,32,5,15,125,51]
sinir = len(ornekListe)

each = 0
count = 0

while (each < sinir):
    count = count + ornekListe[each]
    each = each + 1
