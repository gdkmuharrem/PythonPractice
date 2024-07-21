# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 15:51:53 2024

@author: MUHARREM GEDİK
"""

#%% Quiz2
#Yüzyıl bulan metod yazımı.

#1640.yıl == 17.yy
#109.yıl == 2.yy
#2000.yıl == 20.yy

# input int yıllar, output int y.y
# milattan önce ve 2005'ten sonra dahil edilmeyecek.

def year2century(year):
    """
        year to century
        parameter : year
        output : int century
    """
    str_year = str(year)
    
    if(len(str_year)<3):
        return 1
    elif(len(str_year)==3):
        if(str_year[1:3]=="00"):
            return int(str_year[0])
        else:
            return int(str_year[0])+1
    else:
        if(str_year[2:4]=="00"):
            return int(str_year[0:2])
        else:
            return int(str_year[0:2])+1
        
sonuc = year2century(1900)
print(sonuc)



